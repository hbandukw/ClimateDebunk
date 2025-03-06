import pytest
import yaml
from unittest.mock import patch, MagicMock
from scripts.hyperoptimization import load_config, setup_model_for_hyperopt
from transformers import DistilBertConfig, DistilBertForSequenceClassification

# Sample configuration for testing
sample_config = {
    'data_path': 'path/to/data.parquet',
    'class_col': 'class_col',
    'log_level': 'INFO',
    'save_logs_to_file': False,
    'log_file_path': 'logs/hyperoptim.log',
    'augmenter_model': 'distilbert-base-uncased',
    'augment_action': 'insert',
    'device': 'cpu',
    'output_dir': 'output',
    'n_splits': 5,
    'random_seed': 42,
    'save_intermediate_splits': True
}

def test_load_config(mocker):
    mocker.patch('builtins.open', mocker.mock_open(read_data=yaml.dump(sample_config)))
    config = load_config('path/to/config.yaml')
    assert config == sample_config

@patch('scripts.hyperoptimization.DistilBertForSequenceClassification.from_pretrained')
@patch('scripts.hyperoptimization.DistilBertConfig.from_pretrained')
def test_setup_model_for_hyperopt(mock_config, mock_model):
    # Mock the model and config
    mock_model.return_value = DistilBertForSequenceClassification(DistilBertConfig())
    mock_config.return_value = DistilBertConfig()

    # Call the setup_model_for_hyperopt function
    model = setup_model_for_hyperopt(num_trainable_layers=2, dropout_rate=0.2)

    # Check that the model is set up correctly
    mock_model.assert_called_once_with('distilbert-base-uncased', config=mock_config.return_value)
    mock_config.assert_called_once_with(
        'distilbert-base-uncased',
        num_labels=8,
        dropout=0.2,
        attention_dropout=0.2
    )

    # Check that all layers are initially frozen
    for name, param in model.named_parameters():
        assert not param.requires_grad

    # Check that the specified number of layers are unfrozen
    num_layers = 6  # DistilBERT has 6 layers
    num_trainable_layers = 2
    for layer_idx in range(num_layers - num_trainable_layers, num_layers):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            assert param.requires_grad

    # Check that the classifier layer is unfrozen
    for name, param in model.classifier.named_parameters():
        assert param.requires_grad
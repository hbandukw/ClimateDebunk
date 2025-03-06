import pytest
import torch
from transformers import DistilBertForSequenceClassification, DistilBertConfig
from unittest.mock import patch
from src.model import load_model

# Sample configuration for testing
sample_config = {
    'model_name': 'distilbert-base-uncased',
    'num_labels': 8,
    'dropout_rate': 0.2,
    'num_trainable_layers': 2,
    'total_layers': 6
}

@patch('src.model.config', sample_config)
@patch('src.model.DistilBertForSequenceClassification.from_pretrained')
@patch('src.model.DistilBertConfig.from_pretrained')
def test_load_model(mock_config, mock_model):
    # Mock the model and config
    mock_model.return_value = DistilBertForSequenceClassification(DistilBertConfig())
    mock_config.return_value = DistilBertConfig()

    # Load the model
    model = load_model(sample_config['num_trainable_layers'], sample_config['dropout_rate'])

    # Check that the model is loaded correctly
    mock_model.assert_called_once_with(sample_config['model_name'], config=mock_config.return_value)
    mock_config.assert_called_once_with(
        sample_config['model_name'],
        num_labels=sample_config['num_labels'],
        dropout=sample_config['dropout_rate'],
        attention_dropout=sample_config['dropout_rate']
    )

    # Check that all layers are initially frozen
    for name, param in model.named_parameters():
        assert not param.requires_grad

    # Check that the specified number of layers are unfrozen
    num_layers = sample_config['total_layers']
    num_trainable_layers = sample_config['num_trainable_layers']
    for layer_idx in range(num_layers - num_trainable_layers, num_layers):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            assert param.requires_grad

    # Check that the classifier layer is unfrozen
    for name, param in model.classifier.named_parameters():
        assert param.requires_grad
import pytest
import torch
from transformers import DistilBertConfig, DistilBertForSequenceClassification
from src.model import load_model_for_finetuning, load_model_for_inference

# Fixture for creating a mock config
@pytest.fixture
def mock_config(tmpdir):
    config = {
        'model_name': 'distilbert-base-uncased',
        'num_labels': 2,
        'dropout_rate': 0.1,
        'total_layers': 6,
        'num_trainable_layers': 2,
        'trained_model_path': str(tmpdir.join('trained_model.pth'))
    }
    return config

# Fixture for creating a mock pretrained model for finetuning
@pytest.fixture
def mock_model_for_finetuning(mock_config):
    model_config = DistilBertConfig.from_pretrained(
        mock_config['model_name'],
        num_labels=mock_config['num_labels'],
        dropout=mock_config['dropout_rate'],
        attention_dropout=mock_config['dropout_rate']
    )
    model = DistilBertForSequenceClassification.from_pretrained(
        mock_config['model_name'],
        config=model_config)
    return model

# Fixture for creating a mock trained model file
@pytest.fixture
def mock_model_for_inference(mock_config):
    # Create a dummy model and save its state_dict
    model_config = DistilBertConfig.from_pretrained(
        mock_config['model_name'],
        num_labels=mock_config['num_labels']
    )
    model = DistilBertForSequenceClassification(model_config)
    torch.save(model.state_dict(), mock_config['trained_model_path'])
    return mock_config['trained_model_path']

# Test 1a: Test if the model is initialized with the correct configuration
def test_model_initialization(mock_config, mock_model_for_finetuning):
    model = load_model_for_finetuning(mock_config)
    assert isinstance(model, DistilBertForSequenceClassification)
    assert model.config.num_labels == mock_config['num_labels']

# Test 1b: Test if all the layers are frozen
def test_freeze_all_layers(mock_config, mock_model_for_finetuning):
    model = load_model_for_finetuning(mock_config)
    
    # Check that all parameters are frozen
    for name, param in model.named_parameters():
        assert not param.requires_grad, f"Parameter {name} should be frozen (requires_grad=False)"

# Test 1c: Test if the specified number of transformer layers are unfrozen
def test_unfreeze_transformer_layers(mock_config, mock_model_for_finetuning):
    model = load_model_for_finetuning(mock_config)
    
    total_layers = mock_config['total_layers']
    num_trainable_layers = mock_config['num_trainable_layers']
    
    # Check that the last `num_trainable_layers` are unfrozen e.g. range(4,6) = 4,5
    for layer_idx in range(total_layers - num_trainable_layers, total_layers):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            assert param.requires_grad, f"Layer {layer_idx} should be unfrozen (requires_grad=True)"
    
    # Check that the remaining layers are frozen e.g. range(0, 4) = 0,1,2,3
    for layer_idx in range(0, total_layers - num_trainable_layers):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            assert not param.requires_grad, f"Layer {layer_idx} should be frozen (requires_grad=False)"

# Test 1d: Test if the classifier layer is unfrozen
def test_unfreeze_classifier(mock_config, mock_model_for_finetuning):
    model = load_model_for_finetuning(mock_config)
    
    # Check that the classifier layer is unfrozen
    for name, param in model.classifier.named_parameters():
        assert param.requires_grad, f"Classifier parameter {name} should be unfrozen (requires_grad=True)"

# Test 1e: Edge case where num_trainable_layers = 0
# In this case, all layers should be frozen except the classifier layer
def test_no_trainable_layers(mock_config):
    mock_config['num_trainable_layers'] = 0
    model = load_model_for_finetuning(mock_config)
    
    # Check that no transformer layers are unfrozen
    for layer_idx in range(mock_config['total_layers']):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            assert not param.requires_grad, f"Layer {layer_idx} should be frozen (requires_grad=False)"
    
    # Check that the classifier is still unfrozen
    for name, param in model.classifier.named_parameters():
        assert param.requires_grad, f"Classifier parameter {name} should be unfrozen (requires_grad=True)"

# Test 1f: Edge case where num_trainable_layers = total_layers
# In this case, all transformer layers and the classifier layer should be unfrozen
def test_all_trainable_layers(mock_config):
    mock_config['num_trainable_layers'] = mock_config['total_layers']
    model = load_model_for_finetuning(mock_config)
    
    # Check that all transformer layers are unfrozen
    for layer_idx in range(mock_config['total_layers']):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            assert param.requires_grad, f"Layer {layer_idx} should be unfrozen (requires_grad=True)"
    
    # Check that the classifier is still unfrozen
    for name, param in model.classifier.named_parameters():
        assert param.requires_grad, f"Classifier parameter {name} should be unfrozen (requires_grad=True)"


# Test 2a: Model loads correctly with valid config and trained weights
def test_load_model_for_inference_valid(mock_config, mock_model_for_inference):
    device = 'cpu'
    model = load_model_for_inference(mock_config, device)

    # Check that the model is an instance of DistilBertForSequenceClassification
    assert isinstance(model, DistilBertForSequenceClassification)

    # Check that the model is frozen
    for param in model.parameters():
        assert not param.requires_grad

    # Check that the model is in evaluation mode
    assert not model.training

# Test 2b: Model is loaded onto the correct device
def test_load_model_for_inference_device(mock_config, mock_model_for_inference):
    device = 'cpu'
    model = load_model_for_inference(mock_config, device)

    # Check that all parameters are on the correct device
    for param in model.parameters():
        assert param.device == torch.device(device)

# Test 2c: Handles invalid model path
def test_load_model_for_inference_invalid_path(mock_config):
    mock_config['trained_model_path'] = 'invalid/path/to/model.pt'
    device = 'cpu'

    with pytest.raises(FileNotFoundError):
        load_model_for_inference(mock_config, device)

# Test 2d: Handles missing keys in config
def test_load_model_for_inference_missing_keys():
    invalid_config = {'model_name': 'distilbert-base-uncased'}  # Missing 'num_labels' and 'trained_model_path'
    device = 'cpu'

    with pytest.raises(KeyError):
        load_model_for_inference(invalid_config, device)

# Test 2e: Handles invalid device
def test_load_model_for_inference_invalid_device(mock_config, mock_model_for_inference):
    invalid_device = 'invalid_device'

    with pytest.raises(RuntimeError):
        load_model_for_inference(mock_config, invalid_device)
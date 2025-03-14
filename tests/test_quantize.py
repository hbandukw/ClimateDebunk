import pytest
import torch
import numpy as np
from unittest.mock import MagicMock, patch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from onnxruntime import InferenceSession
from src.quantize import convert_to_onnx, dynamic_quantize, evaluate_onnx_model
from utils import calculate_f1_score

# Mock data for testing
MOCK_CONFIG = {
    'tokenizer_name': 'distilbert-base-uncased',
    'max_length': 128
}
MOCK_QUANTIZE_CONFIG = {
    'onnx_path': 'model.onnx',
    'quantized_onnx_path': 'model_quantized.onnx'
}

# Mock model for testing
MOCK_MODEL = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')

# Mock DataLoader for testing
class MockDataset(Dataset):
    def __init__(self, size=10):
        self.size = size
        self.input_ids = torch.randint(0, 100, (size, MOCK_CONFIG['max_length']))
        self.attention_mask = torch.ones((size, MOCK_CONFIG['max_length']), dtype=torch.int64)
        self.labels = torch.randint(0, 2, (size,))

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return {
            "input_ids": self.input_ids[idx],
            "attention_mask": self.attention_mask[idx],
            "labels": self.labels[idx]
        }

MOCK_VAL_LOADER = DataLoader(MockDataset(), batch_size=2)

# Test convert_to_onnx
def test_convert_to_onnx(mocker):
    """
    Test that the convert_to_onnx function exports the model to ONNX format.
    """
    mock_export = mocker.patch('torch.onnx.export')
    mock_tokenizer = mocker.patch('transformers.DistilBertTokenizer.from_pretrained', return_value=MagicMock())

    convert_to_onnx(MOCK_MODEL, MOCK_CONFIG, MOCK_QUANTIZE_CONFIG)

    # Assertions
    mock_tokenizer.assert_called_once_with(MOCK_CONFIG['tokenizer_name'])
    mock_export.assert_called_once()

# Test dynamic_quantize
def test_dynamic_quantize(mocker):
    """
    Test that the dynamic_quantize function quantizes the ONNX model.
    """
    mock_quantize_dynamic = mocker.patch('onnxruntime.quantization.quantize_dynamic')

    dynamic_quantize(MOCK_QUANTIZE_CONFIG)

    # Assertions
    mock_quantize_dynamic.assert_called_once_with(
        model_input=MOCK_QUANTIZE_CONFIG['onnx_path'],
        model_output=MOCK_QUANTIZE_CONFIG['quantized_onnx_path'],
        weight_type=QuantType.QInt8
    )

# Test evaluate_onnx_model
def test_evaluate_onnx_model(mocker):
    """
    Test that the evaluate_onnx_model function evaluates the ONNX model correctly.
    """
    # Mock ONNX session
    mock_session = MagicMock()
    mock_session.run.return_value = [np.array([[0.6, 0.4], [0.3, 0.7]])]  # Mock logits

    # Mock calculate_f1_score
    mock_f1_score = mocker.patch('utils.calculate_f1_score', return_value=0.85)

    # Call the function
    accuracy, f1, all_val_labels, all_val_preds = evaluate_onnx_model(mock_session, MOCK_VAL_LOADER)

    # Assertions
    assert isinstance(accuracy, float)
    assert isinstance(f1, float)
    assert len(all_val_labels) == 10  # MockDataset size
    assert len(all_val_preds) == 10
    mock_session.run.assert_called()
    mock_f1_score.assert_called_once()

# Test evaluate_onnx_model with empty DataLoader
def test_evaluate_onnx_model_empty_loader(mocker):
    """
    Test that the evaluate_onnx_model function handles an empty DataLoader.
    """
    # Mock ONNX session
    mock_session = MagicMock()

    # Mock empty DataLoader
    empty_loader = DataLoader(MockDataset(size=0), batch_size=2)

    # Call the function
    accuracy, f1, all_val_labels, all_val_preds = evaluate_onnx_model(mock_session, empty_loader)

    # Assertions
    assert accuracy == 0
    assert f1 == 0
    assert len(all_val_labels) == 0
    assert len(all_val_preds) == 0

# Test evaluate_onnx_model with invalid inputs
def test_evaluate_onnx_model_invalid_inputs(mocker):
    """
    Test that the evaluate_onnx_model function handles invalid inputs.
    """
    # Mock ONNX session
    mock_session = MagicMock()
    mock_session.run.side_effect = Exception("Invalid input")

    # Mock DataLoader with invalid inputs
    invalid_loader = DataLoader(MockDataset(), batch_size=2)

    # Call the function and check for exceptions
    with pytest.raises(Exception):
        evaluate_onnx_model(mock_session, invalid_loader)
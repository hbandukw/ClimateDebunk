import pytest
import pandas as pd
import torch
from unittest.mock import patch, MagicMock
from scripts.inference import load_test_data, test_model
from transformers import DistilBertTokenizer

# Sample data for testing
sample_csv_data = pd.DataFrame({
    'quote': ['Climate change is real.', 'We need to act now.'],
    'numeric_label': [1, 2]
})

sample_parquet_data = pd.DataFrame({
    'quote': ['The earth is warming.', 'Renewable energy is the future.'],
    'numeric_label': [1, 2]
})

def test_load_test_data_csv(mocker):
    mocker.patch('pandas.read_csv', return_value=sample_csv_data)
    quotes, labels = load_test_data('sample.csv')
    assert quotes.tolist() == sample_csv_data['quote'].tolist()
    assert labels.tolist() == sample_csv_data['numeric_label'].tolist()

def test_load_test_data_parquet(mocker):
    mocker.patch('pandas.read_parquet', return_value=sample_parquet_data)
    quotes, labels = load_test_data('sample.parquet')
    assert quotes.tolist() == sample_parquet_data['quote'].tolist()
    assert labels.tolist() == sample_parquet_data['numeric_label'].tolist()

@patch('src.inference.calculate_f1_score')
def test_test_model(mock_f1_score):
    # Mock the model and data loader
    mock_model = MagicMock()
    mock_test_loader = MagicMock()
    mock_device = torch.device("cpu")
    mock_f1_score.return_value = 0.8

    # Mock the outputs of the model
    mock_outputs = MagicMock()
    mock_outputs.loss.item.return_value = 0.5
    mock_outputs.logits = torch.tensor([[0.1, 0.9], [0.8, 0.2]])
    mock_model.return_value = mock_outputs

    # Mock the data loader
    mock_batch = {
        'input_ids': torch.tensor([[1, 2, 3], [4, 5, 6]]),
        'attention_mask': torch.tensor([[1, 1, 1], [1, 1, 1]]),
        'labels': torch.tensor([1, 0])
    }
    mock_test_loader.__iter__.return_value = [mock_batch]

    # Run the test_model function
    test_loss, accuracy, f1 = test_model(mock_model, mock_test_loader, mock_device)

    # Check the results
    assert test_loss == 0.5
    assert accuracy == 0.5
    assert f1 == 0.8
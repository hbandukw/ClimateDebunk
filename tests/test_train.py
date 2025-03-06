import pytest
import torch
from unittest.mock import patch, MagicMock
from src.train import main, train_one_epoch, validate_model
from src.model import load_model
from src.data_prep import create_data_loaders
from torch.optim import AdamW, lr_scheduler

# Sample configuration for testing
sample_config = {
    'learning_rate': 1e-4,
    'step_size': 4,
    'gamma': 0.9,
    'epochs': 2,
    'batch_size': 16,
    'max_length': 128,
    'tokenizer_model': 'distilbert-base-uncased',
    'trainpath': 'path/to/train.csv',
    'valpath': 'path/to/val.csv',
    'class_col': 'class_col'
}

@patch('src.train.config', sample_config)
@patch('src.train.load_model')
@patch('src.train.create_data_loaders')
@patch('src.train.AdamW')
@patch('src.train.lr_scheduler.StepLR')
def test_main(mock_scheduler, mock_optimizer, mock_create_data_loaders, mock_load_model):
    # Mock the model, optimizer, scheduler, and data loaders
    mock_model = MagicMock()
    mock_load_model.return_value = mock_model
    mock_optimizer.return_value = MagicMock()
    mock_scheduler.return_value = MagicMock()
    mock_train_loader = MagicMock()
    mock_val_loader = MagicMock()
    mock_create_data_loaders.return_value = (mock_train_loader, mock_val_loader)

    # Run the main function
    main()

    # Check that the model, optimizer, scheduler, and data loaders are set up correctly
    mock_load_model.assert_called_once()
    mock_optimizer.assert_called_once_with(mock_model.parameters(), lr=sample_config['learning_rate'])
    mock_scheduler.assert_called_once_with(mock_optimizer.return_value, step_size=sample_config['step_size'], gamma=sample_config['gamma'])
    mock_create_data_loaders.assert_called_once()

@patch('src.train.calculate_f1_score')
def test_validate_model(mock_f1_score):
    # Mock the model and data loader
    mock_model = MagicMock()
    mock_val_loader = MagicMock()
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
    mock_val_loader.__iter__.return_value = [mock_batch]

    # Run the validate_model function
    average_val_loss, accuracy, f1 = validate_model(mock_model, mock_val_loader, mock_device)

    # Check the results
    assert average_val_loss == 0.5
    assert accuracy == 0.5
    assert f1 == 0.8

@patch('src.train.calculate_f1_score')
def test_train_one_epoch(mock_f1_score):
    # Mock the model, optimizer, and data loader
    mock_model = MagicMock()
    mock_optimizer = MagicMock()
    mock_train_loader = MagicMock()
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
    mock_train_loader.__iter__.return_value = [mock_batch]

    # Run the train_one_epoch function
    average_train_loss, accuracy, f1 = train_one_epoch(mock_model, mock_train_loader, mock_optimizer, mock_device)

    # Check the results
    assert average_train_loss == 0.5
    assert accuracy == 0.5
    assert f1 == 0.8
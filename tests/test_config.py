import pytest
from hyperoptim import objective
from src.config import load_config

# This fixture will mock the Trial object from Optuna.
@pytest.fixture
def mock_trial(mocker):
    mock_trial = mocker.patch('optuna.trial.Trial')
    mock_trial.suggest_float.side_effect = [0.001, 0.1, 0.9]
    mock_trial.suggest_int.side_effect = [2, 10, 5]
    mock_trial.suggest_categorical.side_effect = [32]
    return mock_trial

# This fixture will mock the data loaders.
@pytest.fixture
def mock_data_loaders(mocker):
    mock_create_data_loader = mocker.patch('hyperoptim.create_data_loader')
    mock_train_loader = mocker.MagicMock()
    mock_val_loader = mocker.MagicMock()
    mock_create_data_loader.side_effect = [mock_train_loader, mock_val_loader]
    return mock_train_loader, mock_val_loader

# This fixture will mock the model.
@pytest.fixture
def mock_model(mocker):
    mock_load_model = mocker.patch('hyperoptim.load_model')
    mock_model = mocker.MagicMock()
    mock_load_model.return_value = mock_model
    return mock_model

# This fixture will mock the train_one_epoch and validate_model functions.
@pytest.fixture
def mock_train_validate(mocker):
    mock_train_one_epoch = mocker.patch('hyperoptim.train_one_epoch')
    mock_validate_model = mocker.patch('hyperoptim.validate_model')
    mock_train_one_epoch.return_value = (0.5, 0.8, 0.7)
    mock_validate_model.return_value = (0.4, 0.85, 0.75)
    return mock_train_one_epoch, mock_validate_model

# This test will check if the objective function returns the best validation accuracy.
def test_objective(mock_trial, mock_data_loaders, mock_model, mock_train_validate):
    mock_train_loader, mock_val_loader = mock_data_loaders
    mock_train_one_epoch, mock_validate_model = mock_train_validate

    config = {
        "trainpath": "train.csv",
        "train_label_col": "label",
        "valpath": "val.csv",
        "val_label_col": "label",
        "tokenizer_model": "distilbert-base-uncased",
        "max_length": 128,
        "batch_size": 32,
        "learning_rate": 0.001,
        "step_size": 5,
        "gamma": 0.1
    }

    hyperoptim_config = {
        'learning_rate': {'range': (1e-5, 1e-3), 'log': True},
        'num_trainable_layers': {'range': (1, 12)},
        'dropout_rate': {'range': (0.1, 0.5)},
        'batch_size': {'range': [16, 32, 64]},
        'epochs': {'range': (1, 10)},
        'step_size': {'range': (1, 10)},
        'gamma': {'range': (0.1, 0.9)}
    }

    best_val_accuracy = objective(config, hyperoptim_config, mock_trial)

    assert best_val_accuracy == 0.85
    mock_train_one_epoch.assert_called()
    mock_validate_model.assert_called()
    mock_model.to.assert_called()
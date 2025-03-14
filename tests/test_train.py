import pytest
from pytest_mock import mocker
from sklearn.metrics import accuracy_score
import torch
from src.train import train_one_epoch, validate_model, test_model
from src.utils import calculate_f1_score


# Test 1: Test the train_one_epoch function.
def test_train_one_epoch(mocker):
    # Mock model
    model = mocker.MagicMock()
    model.return_value.loss = torch.tensor(0.5)  # Mock loss
    model.return_value.logits = torch.tensor([[0.6, 0.4], [0.3, 0.7]])  # Mock logits

    # Mock DataLoader
    batch = {
        'input_ids': torch.tensor([[1, 2], [3, 4]]),
        'attention_mask': torch.tensor([[1, 1], [1, 1]]),
        'labels': torch.tensor([0, 1])
    }
    train_loader = mocker.MagicMock()
    train_loader.__len__.return_value = 1
    train_loader.__iter__.return_value = [batch]

    # Mock optimizer
    optimizer = mocker.MagicMock()

    # Call the function
    device = 'cpu'
    avg_loss, accuracy, f1, labels, preds = train_one_epoch(model, train_loader, optimizer, device)

    # Assertions
    assert isinstance(avg_loss, float)
    assert isinstance(accuracy, float)
    assert isinstance(f1, float)
    assert len(labels) == 2
    assert len(preds) == 2
    assert 0 <= accuracy <= 1
    assert 0 <= f1 <= 1
    optimizer.zero_grad.assert_called_once()
    optimizer.step.assert_called_once()

# Test 2: Test the validate_model function.
def test_validate_model(mocker):
    # Mock model
    model = mocker.MagicMock()
    model.return_value.loss = torch.tensor(0.5)  # Mock loss
    model.return_value.logits = torch.tensor([[0.6, 0.4], [0.3, 0.7]])  # Mock logits

    # Mock DataLoader
    batch = {
        'input_ids': torch.tensor([[1, 2], [3, 4]]),
        'attention_mask': torch.tensor([[1, 1], [1, 1]]),
        'labels': torch.tensor([0, 1])
    }
    val_loader = mocker.MagicMock()
    val_loader.__len__.return_value = 1
    val_loader.__iter__.return_value = [batch]

    # Call the function
    device = 'cpu'
    avg_loss, accuracy, f1, labels, preds = validate_model(model, val_loader, device)

    # Assertions
    assert isinstance(avg_loss, float)
    assert isinstance(accuracy, float)
    assert isinstance(f1, float)
    assert len(labels) == 2
    assert len(preds) == 2
    assert 0 <= accuracy <= 1
    assert 0 <= f1 <= 1

# Test 3: Test the test_model function.
def test_test_model(mocker):
    # Mock model
    model = mocker.MagicMock()
    model.return_value.logits = torch.tensor([[0.6, 0.4], [0.3, 0.7]])  # Mock logits

    # Mock DataLoader
    batch = (
        torch.tensor([[1, 2], [3, 4]]),  # input_ids
        torch.tensor([[1, 1], [1, 1]]),  # attention_mask
        torch.tensor([0, 1])  # labels
    )
    test_loader = mocker.MagicMock()
    test_loader.__iter__.return_value = [batch]

    # Mock accuracy_score and calculate_f1_score
    mocker.patch('sklearn.metrics.accuracy_score', return_value=0.85)
    mocker.patch('utils.calculate_f1_score', return_value=0.8)

    # Call the function
    device = 'cpu'
    accuracy, f1, y_true, y_pred = test_model(model, test_loader, device)

    # Assertions
    assert isinstance(accuracy, float)
    assert isinstance(f1, float)
    assert len(y_true) == 2
    assert len(y_pred) == 2
    assert 0 <= accuracy <= 1
    assert 0 <= f1 <= 1
    model.eval.assert_called_once()
    model.to.assert_called_once_with(device)

# Test 4: Test the train_one_epoch function with an empty DataLoader.
def test_train_one_epoch_empty_loader(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock empty DataLoader
    train_loader = mocker.MagicMock()
    train_loader.__len__.return_value = 0
    train_loader.__iter__.return_value = []

    # Mock optimizer
    optimizer = mocker.MagicMock()

    # Call the function
    device = 'cpu'
    avg_loss, accuracy, f1, labels, preds = train_one_epoch(model, train_loader, optimizer, device)

    # Assertions
    assert avg_loss == 0
    assert accuracy == 0
    assert f1 == 0
    assert len(labels) == 0
    assert len(preds) == 0

# Test 5: Test the train_one_epoch function with missing 'labels' in batch. 
def test_train_one_epoch_missing_labels(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock DataLoader with missing 'labels'
    batch = {
        'input_ids': torch.tensor([[1, 2], [3, 4]]),
        'attention_mask': torch.tensor([[1, 1], [1, 1]])
    }
    train_loader = mocker.MagicMock()
    train_loader.__len__.return_value = 1
    train_loader.__iter__.return_value = [batch]

    # Mock optimizer
    optimizer = mocker.MagicMock()

    # Call the function and check for KeyError
    device = 'cpu'
    with pytest.raises(KeyError):
        train_one_epoch(model, train_loader, optimizer, device)

# Test 6: Test the train_one_epoch function with invalid batch structure.
def test_train_one_epoch_invalid_batch_structure(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock DataLoader with invalid batch structure
    batch = {
        'input_ids': torch.tensor([[1, 2], [3, 4]]),
        'attention_mask': torch.tensor([[1, 1], [1, 1]])
        # Missing 'labels'
    }
    train_loader = mocker.MagicMock()
    train_loader.__len__.return_value = 1
    train_loader.__iter__.return_value = [batch]

    # Mock optimizer
    optimizer = mocker.MagicMock()

    # Call the function and check for KeyError
    device = 'cpu'
    with pytest.raises(KeyError):
        train_one_epoch(model, train_loader, optimizer, device)

# Test 7: Test the validate_model function with an empty DataLoader.
def test_validate_model_empty_loader(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock empty DataLoader
    val_loader = mocker.MagicMock()
    val_loader.__len__.return_value = 0
    val_loader.__iter__.return_value = []

    # Call the function
    device = 'cpu'
    avg_loss, accuracy, f1, labels, preds = validate_model(model, val_loader, device)

    # Assertions
    assert avg_loss == 0
    assert accuracy == 0
    assert f1 == 0
    assert len(labels) == 0
    assert len(preds) == 0

# Test 8: Test the validate_model function with missing 'labels' in batch.
def test_validate_model_missing_labels(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock DataLoader with missing 'labels'
    batch = {
        'input_ids': torch.tensor([[1, 2], [3, 4]]),
        'attention_mask': torch.tensor([[1, 1], [1, 1]])
        # Missing 'labels'
    }
    val_loader = mocker.MagicMock()
    val_loader.__len__.return_value = 1
    val_loader.__iter__.return_value = [batch]

    # Call the function and check for KeyError
    device = 'cpu'
    with pytest.raises(KeyError):
        validate_model(model, val_loader, device)

# Test 9: Test the validate_model function with invalid batch structure.
def test_validate_model_invalid_batch_structure(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock DataLoader with invalid batch structure
    batch = {
        'input_ids': torch.tensor([[1, 2], [3, 4]]),
        # Missing 'attention_mask' and 'labels'
    }
    val_loader = mocker.MagicMock()
    val_loader.__len__.return_value = 1
    val_loader.__iter__.return_value = [batch]

    # Call the function and check for KeyError
    device = 'cpu'
    with pytest.raises(KeyError):
        validate_model(model, val_loader, device)

# Test 10: Test the test_model function with an empty DataLoader.
def test_test_model_empty_loader(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock empty DataLoader
    test_loader = mocker.MagicMock()
    test_loader.__iter__.return_value = []

    # Mock accuracy_score and calculate_f1_score
    mocker.patch('sklearn.metrics.accuracy_score', return_value=0.0)
    mocker.patch('utils.calculate_f1_score', return_value=0.0)

    # Call the function
    device = 'cpu'
    accuracy, f1, y_true, y_pred = test_model(model, test_loader, device)

    # Assertions
    assert accuracy == 0
    assert f1 == 0
    assert len(y_true) == 0
    assert len(y_pred) == 0

# Test 11: Test the test_model function with an invalid batch structure.
def test_test_model_invalid_batch_structure(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock DataLoader with invalid batch structure
    batch = (
        torch.tensor([[1, 2], [3, 4]]),  # input_ids
        # Missing 'attention_mask' and 'labels'
    )
    test_loader = mocker.MagicMock()
    test_loader.__iter__.return_value = [batch]

    # Call the function and check for ValueError
    device = 'cpu'
    with pytest.raises(ValueError):
        test_model(model, test_loader, device)

# Test 12: Test the test_model function with missing 'labels' in batch.
def test_test_model_missing_labels(mocker):
    # Mock model
    model = mocker.MagicMock()

    # Mock DataLoader with missing 'labels'
    batch = (
        torch.tensor([[1, 2], [3, 4]]),  # input_ids
        torch.tensor([[1, 1], [1, 1]]),  # attention_mask
        # Missing 'labels'
    )
    test_loader = mocker.MagicMock()
    test_loader.__iter__.return_value = [batch]

    # Call the function and check for ValueError
    device = 'cpu'
    with pytest.raises(ValueError):
        test_model(model, test_loader, device)
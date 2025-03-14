import os
import torch
from utils import calculate_f1_score
from sklearn.metrics import accuracy_score

def train_one_epoch(model, train_loader, optimizer, device):
    """
    Trains the model for one epoch using the provided data loader for training data and the optimizer.

    Args:
        model (torch.nn.Module): The model to train.
        train_loader (torch.utils.data.DataLoader): The data loader providing training batches.
        optimizer (torch.optim.Optimizer): The optimizer used to update the model parameters.
        device (torch.device or str): The device to use for training (e.g., 'cpu' or 'cuda').

    Returns:
        tuple: A tuple containing the following metrics:
            - average_train_loss (float): The average training loss for the epoch.
            - train_accuracy (float): The training accuracy for the epoch.
            - train_f1 (float): The training F1 score for the epoch.
            - all_train_labels (list): A list of all ground truth labels in the epoch.
            - all_train_preds (list): A list of all predicted labels in the epoch.

    Notes:
        - The model is set to training mode (`model.train()`) at the start of the epoch.
        - The optimizer's gradients are zeroed before each batch (`optimizer.zero_grad()`).
        - The loss is computed using the model's output (`outputs.loss`), and the model parameters are updated using `loss.backward()` and `optimizer.step()`.
        - Training metrics (loss, accuracy, F1 score) are computed and returned for the entire epoch.
        - The function assumes that `calculate_f1_score` is defined elsewhere or imported.
    
    """
    model.train()
    train_loss = 0
    correct_train = 0
    total_train = 0
    all_train_labels = []
    all_train_preds = []
    for batch in train_loader:
        optimizer.zero_grad()
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        predictions = torch.argmax(outputs.logits, dim=-1)
        correct_train += (predictions == batch['labels']).sum().item()
        total_train += batch['labels'].size(0)
        all_train_labels.extend(batch['labels'].cpu().numpy())
        all_train_preds.extend(predictions.cpu().numpy())
    average_train_loss = train_loss / len(train_loader)
    train_accuracy = correct_train / total_train
    train_f1 = calculate_f1_score(all_train_labels, all_train_preds)
    return average_train_loss, train_accuracy, train_f1, all_train_labels, all_train_preds


def validate_model(model, val_loader, device):
    """
    Validates the model using the data loader for validation data.
    
    Args:
        model (torch.nn.Module): The model to validate.
        val_loader (torch.utils.data.DataLoader): The data loader providing validation batches.
        device (torch.device or str): The device to use for validation (e.g., 'cpu' or 'cuda').
    
    Returns:
        tuple: A tuple containing the following metrics:
            - average_val_loss (float): The average validation loss.
            - val_accuracy (float): The validation accuracy.
            - val_f1 (float): The validation F1 score.
            - all_val_labels (list): A list of all ground truth labels in the validation set.
            - all_val_preds (list): A list of all predicted labels in the validation set.
    Notes:
        - The model is set to evaluation mode (`model.eval()`) before validation.
        - The function computes the validation loss and validation accuracy for the entire validation set.
        
    """
    model.eval()
    val_loss = 0
    correct_val = 0
    total_val = 0
    all_val_labels = []
    all_val_preds = []
    with torch.no_grad():
        for batch in val_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            val_loss += outputs.loss.item()
            predictions = torch.argmax(outputs.logits, dim=-1)
            correct_val += (predictions == batch['labels']).sum().item()
            total_val += batch['labels'].size(0)
            all_val_labels.extend(batch['labels'].cpu().numpy())
            all_val_preds.extend(predictions.cpu().numpy())
    average_val_loss = val_loss / len(val_loader)
    val_accuracy = correct_val / total_val
    val_f1 = calculate_f1_score(all_val_labels, all_val_preds)
    return average_val_loss, val_accuracy, val_f1, all_val_labels, all_val_preds

def test_model(model, test_loader, device):
    """
    Evaluates the model on the provided test data loader.

    Args:
        model (torch.nn.Module): The model to evaluate.
        test_loader (torch.utils.data.DataLoader): The data loader providing test batches.
        device (torch.device or str): The device to use for evaluation (e.g., 'cpu' or 'cuda').

    Returns:
        tuple: A tuple containing the following metrics:
            - accuracy (float): The accuracy of the model on the test set.
            - f1 (float): The F1 score of the model on the test set.
            - y_true (list): A list of all ground truth labels in the test set.
            - y_pred (list): A list of all predicted labels in the test set.

    """
    model.eval()
    model.to(device)
    y_true, y_pred = [], []
    with torch.no_grad():
        for batch in test_loader:
            input_ids, attention_mask, labels = [x.to(device) for x in batch]
            outputs = model(input_ids, attention_mask=attention_mask)
            preds = torch.argmax(outputs.logits, dim=1)
            
            y_true.extend(labels.cpu().numpy())
            y_pred.extend(preds.cpu().numpy())

        accuracy = accuracy_score(y_true, y_pred)
        f1 = calculate_f1_score(y_true, y_pred)
        print(f"Test Accuracy: {accuracy:.4f}")
        print(f"Test F1 Score: {f1:.4f}")

        return accuracy, f1, y_true, y_pred
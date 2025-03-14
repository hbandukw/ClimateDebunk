import os
import torch
from utils import calculate_f1_score
from sklearn.metrics import accuracy_score

def train_one_epoch(model, train_loader, optimizer, device):
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
    return average_train_loss, train_accuracy, train_f1


def validate_model(model, val_loader, device):
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
    return average_val_loss, val_accuracy, val_f1

def test_model(model, test_loader, device):
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
            print(f"Test Accuracy: {accuracy:.4f}")
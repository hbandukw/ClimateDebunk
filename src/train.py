import os
import torch
from torch.optim import AdamW, lr_scheduler
from .model import load_model
from .data_prep import create_trainloader, create_valloader
from .utils import plot_loss, plot_accuracy, calculate_f1_score
from . import config

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
    average_loss = train_loss / len(train_loader)
    accuracy = correct_train / total_train
    f1 = calculate_f1_score(all_train_labels, all_train_preds)
    return average_loss, accuracy, f1


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
    accuracy = correct_val / total_val
    f1 = calculate_f1_score(all_val_labels, all_val_preds)
    return average_val_loss, accuracy, f1


def main():
    model = load_model()
    optimizer = AdamW(model.parameters(), lr=config['learning_rate'])
    scheduler = lr_scheduler.StepLR(optimizer, step_size=config['step_size'], gamma=config['gamma'])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    train_loader = create_trainloader(config["trainpath"], 
                                      config["class_col"],
                                      config['tokenizer_model'],
                                      config['max_length'],
                                      config['batch_size'],
                                      shuffle=True)
    

    val_loader = create_valloader(config["valpath"], 
                                  config["class_col"],
                                  config['tokenizer_model'],
                                  config['max_length'],
                                  config['batch_size'],
                                  shuffle=False) 

    train_losses = []
    val_losses = []
    train_accuracies = []
    val_accuracies = []
    train_f1_scores = []
    val_f1_scores = []

    for epoch in range(config['epochs']):
        train_loss, train_accuracy, train_f1 = train_one_epoch(model, train_loader, optimizer, device)
        val_loss, val_accuracy, val_f1 = validate_model(model, val_loader, device)
        train_losses.append(train_loss)
        val_losses.append(val_loss)
        train_accuracies.append(train_accuracy)
        val_accuracies.append(val_accuracy)
        train_f1_scores.append(train_f1)
        val_f1_scores.append(val_f1)
        print(f"Epoch {epoch+1}/{config['epochs']}, Train Loss: {train_loss}, Train Accuracy: {train_accuracy}, Train F1: {train_f1}, Val Loss: {val_loss}, Val Accuracy: {val_accuracy}, Val F1: {val_f1}")

    plot_loss(train_losses, val_losses, config['epochs'])
    plot_accuracy(train_accuracies, val_accuracies, config['epochs'])
    
    # Save the trained model
    torch.save(model.state_dict(), config['trained_model_path'])
    print(f"Model saved as {config['trained_model_path']}")

if __name__ == "__main__":
    main()

import os
import pandas as pd
import numpy as np
import torch
import torch.nn.utils.prune as prune
from torch.optim import AdamW, lr_scheduler
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, DistilBertConfig
from data_prep import create_data_loader
from model import load_model
from train import train_one_epoch, validate_model


def objective(config, hyperoptim_config, trial):
    learning_rate = trial.suggest_float('learning_rate', *hyperoptim_config['learning_rate']['range'], log=hyperoptim_config['learning_rate']['log'])
    num_trainable_layers = trial.suggest_int('num_trainable_layers', *hyperoptim_config['num_trainable_layers']['range'])
    dropout_rate = trial.suggest_float('dropout_rate', *hyperoptim_config['dropout_rate']['range'])
    batch_size = trial.suggest_categorical('batch_size', *hyperoptim_config['batch_size']['range'])
    epochs = trial.suggest_int('epochs', *hyperoptim_config['epochs']['range'])
    step_size = trial.suggest_int('step_size', *hyperoptim_config['step_size']['range'])
    gamma = trial.suggest_float('gamma', *hyperoptim_config['gamma']['range'])

    # Load training and validation data
    train_loader = create_data_loader(config["trainpath"], 
                                        config["train_label_col"],
                                        config['tokenizer_model'],
                                        config['max_length'],
                                        config['batch_size'],
                                        shuffle=True)

    val_loader = create_data_loader(config["valpath"], 
                                    config["val_label_col"],
                                    config['tokenizer_model'],
                                    config['max_length'],
                                    config['batch_size'],
                                    shuffle=False) 

    # load model
    model = load_model(config)

    # define scheduler and optimizer
    optimizer = AdamW(model.parameters(), lr=config['learning_rate'])
    scheduler = lr_scheduler.StepLR(optimizer, step_size=config['step_size'], gamma=config['gamma'])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    val_accuracies = []
    for epoch in range(epochs):
        average_train_loss, train_accuracy, train_f1 = train_one_epoch(model, train_loader, optimizer, device)
        average_val_loss, val_accuracy, val_f1 = validate_model(model, val_loader, device)
        scheduler.step()
        val_accuracies.append(val_accuracy)
    
    best_val_accuracy = max(val_accuracies)
    
    return best_val_accuracy


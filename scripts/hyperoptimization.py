# Script used for getting optimal hyperparameters

import os
import pandas as pd
import numpy as np
import torch
import torch.nn.utils.prune as prune
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW, lr_scheduler
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, DistilBertConfig
from sklearn.metrics import f1_score, confusion_matrix, balanced_accuracy_score, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import optuna
import shutil
import zipfile
import yaml

from src.data_prep import read_train_data, read_val_data

# Load configuration
def load_config(config_path="configs/hyperoptim_config.yaml"):
    """Loads YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def setup_model_for_hyperopt(num_trainable_layers, dropout_rate):
    config = DistilBertConfig.from_pretrained(
        'distilbert-base-uncased',
        num_labels=8,
        dropout=dropout_rate,
        attention_dropout=dropout_rate
    )
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', config=config)
    for name, param in model.named_parameters():
        param.requires_grad = False
    for layer_idx in range(6 - num_trainable_layers, 6):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            param.requires_grad = True
    for name, param in model.classifier.named_parameters():
        param.requires_grad = True
    return model


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

# Load configuration
def load_config(config_path="configs/hyperoptim_config.yaml"):
    """Loads YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def read_train_data(trainpath):
    texts = []
    labels = []
    for i in range(5):
        df = pd.read_csv(f"{trainpath}/df_balanced{i}.csv")
        texts.append(df['quote'])
        labels.append(df['numeric_label'])
    
    texts_combined = pd.concat(texts, ignore_index=True)
    labels_combined = pd.concat(labels, ignore_index=True)

    return texts_combined, labels_combined

def read_val_data(valpath):
    df = pd.read_parquet(valpath)
    df['label_int'] = df['label'].str.split("_").str[0].astype('int')

    texts = df["quote"].to_list()
    labels = df["label_int"].to_list()


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
import torch
from torch.utils.data import DataLoader, Dataset
#from transformers import BertTokenizer, BertForSequenceClassification, AdamW
#from sklearn.model_selection import train_test_split, KFold
import pandas as pd
import numpy as np
import re
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import matplotlib.pyplot as plt
#from sklearn.metrics import f1_score
#import nlpaug.augmenter.word as naw
#from sklearn.model_selection import KFold
import os
import yaml
import argparse


# Load configuration
def load_config(config_path="configs/config.yaml"):
    """Loads YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def read_train_data(trainpath):
    if "kaggle" in trainpath:
        train = pd.read_csv(trainpath)
    if "huggingface" in trainpath:
        train = pd.read_parquet(trainpath)

    return train['quote'], train['numeric_label']

def read_val_data(valpath):
    val = pd.read_parquet(valpath)
    val['label_int'] = val['label'].str.split("_").str[0].astype('int')

    return val["quote"], val["label_int"]

# Dataset and DataLoader preparation
class QuotesDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

    def __len__(self):
        return len(self.labels)

def encode_data(tokenizer, texts, labels, max_length):
    try:
        if isinstance(texts, pd.Series):
            texts = texts.tolist()
        if isinstance(labels, pd.Series):
            labels = labels.tolist()
            
        encodings = tokenizer(texts, truncation=True, padding='max_length', max_length=max_length, return_tensors='pt')
        return QuotesDataset(encodings, labels)

    except Exception as e:
        print(f"Error during tokenization: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="encodes data")
    parser.add_argument("--config", type=str, default="configs/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)

    train_texts, train_labels = read_train_data(config["trainpath"])
    val_texts, val_labels = read_val_data(config["valpath"])

    tokenizer = DistilBertTokenizer.from_pretrained(config["tokenizer_model"], do_lower_case=True)

    train_dataset = encode_data(tokenizer, train_texts, train_labels, config["max_length"])
    val_dataset = encode_data(tokenizer, val_texts, val_labels, config["max_length"])


    

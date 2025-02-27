import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split, KFold
import pandas as pd
import numpy as np
import re
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
import nlpaug.augmenter.word as naw
from sklearn.model_selection import KFold
import os



tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased', do_lower_case=True)
MAX_LENGTH = 365

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


train_dataset = encode_data(tokenizer, text_combined, label_combined, MAX_LENGTH)
val_dataset = encode_data(tokenizer, texts, labels, MAX_LENGTH)


    

import torch
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from transformers import DistilBertTokenizer
from . import config

def read_data(filepath: str, label_column: str):
    """Reads data from the specified path and processes labels if necessary."""
    try:
        if filepath.endswith('.csv'):
            data = pd.read_csv(filepath)
        elif filepath.endswith('.parquet'):
            data = pd.read_parquet(filepath)
            data = process_labels(data, label_column)
        else:
            raise ValueError("Unsupported file type. Only CSV and Parquet are supported.")
        return data
    except Exception as e:
        raise RuntimeError(f"Error reading data from {filepath}: {e}")

def process_labels(data, label_column: str):
    """Processes labels in the data."""
    if label_column in data.columns:
        data['numeric_label'] = data[label_column].str.split("_").str[0].astype('int')
    return data

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
        encodings = tokenizer(texts, truncation=True, padding='max_length', max_length=max_length, return_tensors='pt')
        return QuotesDataset(encodings, labels)
    except Exception as e:
        print(f"Error during tokenization: {e}")
        return None

def create_data_loaders():
    """Creates and returns DataLoader for PyTorch."""
    train_data = read_data(config["trainpath"], config["class_col"])
    val_data = read_data(config["valpath"], config["class_col"])

    tokenizer = DistilBertTokenizer.from_pretrained(config["tokenizer_model"], do_lower_case=True)

    train_dataset = encode_data(tokenizer, train_data['quote'], train_data['numeric_label'], config["max_length"])
    val_dataset = encode_data(tokenizer, val_data['quote'], val_data['numeric_label'], config["max_length"])

    train_loader = DataLoader(train_dataset, batch_size=config["batch_size"], shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=config["batch_size"], shuffle=False)

    return train_loader, val_loader

    

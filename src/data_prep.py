import torch
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from transformers import DistilBertTokenizer

def read_data(filepath: str, label_column: str):
    """Reads data from the specified path and processes labels if necessary."""
    try:
        if filepath.endswith('.csv'):
            data = pd.read_csv(filepath)
        elif filepath.endswith('.parquet'):
            data = pd.read_parquet(filepath)
        else:
            raise ValueError("Unsupported file type. Only CSV and Parquet are supported.")
        
        # check if label column exists
        if label_column not in data.columns:
            raise ValueError(f"Label column {label_column} not found in the data.")
        
        # Check if the label column is numeric
        if pd.api.types.is_numeric_dtype(data[label_column]):
            data.rename(columns={label_column: 'numeric_label'}, inplace=True)
        else:
            data = process_labels(data, label_column)
        
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
        if isinstance(texts, pd.Series):
            texts = texts.tolist()
        if isinstance(labels, pd.Series):
            labels = labels.tolist()

        encodings = tokenizer(texts, truncation=True, padding='max_length', max_length=max_length, return_tensors='pt')
        return QuotesDataset(encodings, labels)
    except Exception as e:
        print(f"Error during tokenization: {e}")
        return None

def create_data_loader(filepath, label_column, tokenizer_model, max_length, batch_size, shuffle : bool):
    data = read_data(filepath, label_column)
    if data is None or data.empty:
        raise ValueError(f"Data is empty or not loaded correctly from {filepath}")
    print(f"Data loaded successfully from {filepath}")
    tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_model, do_lower_case=True)
    dataset = encode_data(tokenizer, data['quote'], data['numeric_label'], max_length)
    if dataset is None or len(dataset) == 0:
        raise ValueError("Dataset is empty or not created correctly.")
    print(f"Dataset created successfully with {len(dataset)} samples")
    
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return dataloader


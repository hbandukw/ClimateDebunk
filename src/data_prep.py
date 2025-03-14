import torch
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from transformers import DistilBertTokenizer

def read_data(filepath: str, label_column: str):
    """
    Reads data from the specified path and processes labels if necessary.

    Args:
        filepath (str): The path to the data file. Supported formats are CSV and Parquet.
        label_column (str): The name of the column containing the labels.

    Returns:
        pd.DataFrame: The data read from the file with processed labels.

    Raises:
        ValueError: If the file type is not supported or the label column is not found.
        RuntimeError: If there is an error reading the data from the file.
    """
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
    """
    Processes labels in the data by extracting numeric values from a specified label column.

    Args:
        data (pandas.DataFrame): The input data containing the labels.
        label_column (str): The name of the column containing the labels to be processed.

    Returns:
        pandas.DataFrame: The data with an additional column 'numeric_label' containing the extracted numeric values.
    """
    if label_column in data.columns:
        data['numeric_label'] = data[label_column].str.split("_").str[0].astype('int')
    return data

# Dataset and DataLoader preparation
class QuotesDataset(Dataset):
    """
    A custom Dataset class for handling quotes data.

    Args:
        encodings (dict): A dictionary containing the encoded input data.
        labels (list): A list of labels corresponding to the input data.

    Methods:
        __getitem__(idx):
            Retrieves the item (input data and label) at the specified index.
            Args:
                idx (int): The index of the item to retrieve.
            Returns:
                dict: A dictionary containing the input data and label for the specified index.

        __len__():
            Returns the total number of items in the dataset.
            Returns:
                int: The number of items in the dataset.
    """
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
    """
    Encodes text data using a specified tokenizer and prepares it for model input.

    Args:
        tokenizer (PreTrainedTokenizer): The tokenizer to use for encoding the texts.
        texts (Union[List[str], pd.Series]): The texts to be tokenized.
        labels (Union[List[int], pd.Series]): The labels corresponding to the texts.
        max_length (int): The maximum length for the tokenized sequences.

    Returns:
        QuotesDataset: A dataset containing the tokenized texts and their corresponding labels.
        None: If an error occurs during tokenization, None is returned.

    Raises:
        Exception: If an error occurs during tokenization, it is caught and printed.
    """
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
    def create_data_loader(filepath, label_column, tokenizer_model, max_length, batch_size, shuffle: bool):
        """
        Creates a DataLoader for the given dataset.
        Args:
            filepath (str): Path to the data file.
            label_column (str): Name of the column containing the labels.
            tokenizer_model (str): Name or path of the tokenizer model to use.
            max_length (int): Maximum length of the tokenized sequences.
            batch_size (int): Number of samples per batch.
            shuffle (bool): Whether to shuffle the data.
        Returns:
            DataLoader: A DataLoader object for the dataset.
        Raises:
            ValueError: If the data is empty or not loaded correctly.
            ValueError: If the dataset is empty or not created correctly.
        """
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


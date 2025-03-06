import pytest
import pandas as pd
from src.data_prep import read_data, process_labels, encode_data, QuotesDataset, create_data_loaders
from transformers import DistilBertTokenizer
from unittest.mock import patch

# Sample data for testing
sample_csv_data = pd.DataFrame({
    'quote': ['Climate change is real.', 'We need to act now.'],
    'class_col': ['1_climate', '2_action']
})

sample_parquet_data = pd.DataFrame({
    'quote': ['The earth is warming.', 'Renewable energy is the future.'],
    'class_col': ['1_climate', '2_energy']
})

def test_read_data_csv(mocker):
    mocker.patch('pandas.read_csv', return_value=sample_csv_data)
    data = read_data('sample.csv', 'class_col')
    assert not data.empty
    assert 'numeric_label' not in data.columns

def test_read_data_parquet(mocker):
    mocker.patch('pandas.read_parquet', return_value=sample_parquet_data)
    data = read_data('sample.parquet', 'class_col')
    assert not data.empty
    assert 'numeric_label' in data.columns
    assert data['numeric_label'].tolist() == [1, 2]

def test_process_labels():
    data = process_labels(sample_parquet_data.copy(), 'class_col')
    assert 'numeric_label' in data.columns
    assert data['numeric_label'].tolist() == [1, 2]

def test_encode_data():
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    texts = sample_csv_data['quote'].tolist()
    labels = [1, 2]
    dataset = encode_data(tokenizer, texts, labels, max_length=10)
    assert isinstance(dataset, QuotesDataset)
    assert len(dataset) == 2
    assert 'labels' in dataset[0]

def test_quotes_dataset():
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    texts = sample_csv_data['quote'].tolist()
    labels = [1, 2]
    encodings = tokenizer(texts, truncation=True, padding='max_length', max_length=10, return_tensors='pt')
    dataset = QuotesDataset(encodings, labels)
    assert len(dataset) == 2
    assert 'labels' in dataset[0]
    assert dataset[0]['labels'].item() == 1
    
@patch('src.data_prep.read_data')
@patch('src.data_prep.DistilBertTokenizer.from_pretrained')
def test_create_data_loaders(mock_tokenizer, mock_read_data):
    mock_read_data.side_effect = [sample_csv_data, sample_parquet_data]
    mock_tokenizer.return_value = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    train_loader, val_loader = create_data_loaders(sample_csv_data, sample_parquet_data)
    assert len(train_loader.dataset) == len(sample_csv_data)
    assert len(val_loader.dataset) == len(sample_parquet_data)
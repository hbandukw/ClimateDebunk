import pytest
import pandas as pd
from transformers import DistilBertTokenizer
from torch.utils.data import DataLoader
from src.data_prep import read_data, process_labels, QuotesDataset, encode_data, create_data_loader

# Fixture for csv and parquet data, paths, and tokenizer. 
@pytest.fixture
def setup_data():
    csv_data = pd.DataFrame({
        'quote': ['Climate change is real', 'We need to act now'],
        'label': ['1_positive', '0_negative']
    })
    csv_path = '/tmp/test_data.csv'
    csv_data.to_csv(csv_path, index=False)

    parquet_data = pd.DataFrame({
        'quote': ['Climate change is real', 'We need to act now'],
        'label': ['1_positive', '0_negative']
    })
    parquet_path = '/tmp/test_data.parquet'
    parquet_data.to_parquet(parquet_path, index=False)

    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

    return csv_data, csv_path, parquet_data, parquet_path, tokenizer

# Test 1: That the function reads data from a CSV file and returns a DataFrame.
def test_read_data_csv(setup_data):
    _, csv_path, _, _, _ = setup_data
    data = read_data(csv_path, 'label')
    assert not data.empty
    assert 'numeric_label' in data.columns
    assert data['numeric_label'].iloc[0] == 1

# Test 2: That the function reads data from a Parquet file and returns a DataFrame.
def test_read_data_parquet(setup_data):
    _, _, _, parquet_path, _ = setup_data
    data = read_data(parquet_path, 'label')
    assert not data.empty
    assert 'numeric_label' in data.columns
    assert data['numeric_label'].iloc[0] == 1

# Test 3: That the function raises a ValueError when an invalid file type is provided.
def test_read_data_invalid_file_type():
    with pytest.raises(ValueError):
        read_data('/tmp/test_data.txt', 'label')

# Test 4: That the function raises a ValueError when the label column is missing.
def test_read_data_missing_label_column(setup_data):
    _, csv_path, _, _, _ = setup_data
    with pytest.raises(ValueError):
        read_data(csv_path, 'missing_label')

# Test 5: That the function processes the labels correctly.
def test_process_labels(setup_data):
    csv_data, _, _, _, _ = setup_data
    data = process_labels(csv_data, 'label')
    assert 'numeric_label' in data.columns
    assert data['numeric_label'].iloc[0] == 1

# Test 6: That the function encodes the data correctly.
def test_encode_data(setup_data):
    csv_data, _, _, _, tokenizer = setup_data
    texts = csv_data['quote']
    labels = [1, 0]
    dataset = encode_data(tokenizer, texts, labels, max_length=10)
    assert isinstance(dataset, QuotesDataset)
    assert len(dataset) == 2

# Test 7: That the function creates a DataLoader object.
def test_create_data_loader(setup_data):
    _, csv_path, _, _, _ = setup_data
    dataloader = create_data_loader(csv_path, 'label', 'distilbert-base-uncased', max_length=10, batch_size=2, shuffle=False)
    assert isinstance(dataloader, DataLoader)
    assert len(dataloader.dataset) == 2
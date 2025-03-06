import pytest
import yaml
import pandas as pd
from unittest.mock import patch, MagicMock
from scripts.augment_train import load_config, extract_number, balance_dataset

# Sample configuration for testing
sample_config = {
    'data_path': 'path/to/data.parquet',
    'class_col': 'class_col',
    'log_level': 'INFO',
    'save_logs_to_file': False,
    'log_file_path': 'logs/augmentation.log',
    'augmenter_model': 'distilbert-base-uncased',
    'augment_action': 'insert',
    'device': 'cpu',
    'output_dir': 'output',
    'n_splits': 5,
    'random_seed': 42,
    'save_intermediate_splits': True
}

# Sample data for testing
sample_data = pd.DataFrame({
    'quote': ['Climate change is real.', 'We need to act now.'],
    'class_col': ['1_climate', '2_action']
})

def test_load_config(mocker):
    mocker.patch('builtins.open', mocker.mock_open(read_data=yaml.dump(sample_config)))
    config = load_config('path/to/config.yaml')
    assert config == sample_config

def test_extract_number():
    assert extract_number('1_climate') == 1
    assert extract_number('2_action') == 2
    assert extract_number('no_number') is None

@patch('scripts.augment_train.nlpaug.augmenter.word.ContextualWordEmbsAug')
def test_balance_dataset(mock_augmenter):
    mock_augmenter.return_value.augment.side_effect = lambda x: [f'augmented_{x}']
    balanced_data = balance_dataset(sample_data, 'class_col', 'quote', mock_augmenter.return_value)
    
    # Check that the augmented data has the correct number of rows
    assert len(balanced_data) == len(sample_data) * 2
    
    # Check that the augmented data contains the augmented text
    augmented_texts = balanced_data[balanced_data['quote'].str.startswith('augmented_')]['quote']
    assert len(augmented_texts) == len(sample_data)
    
    # Check that the numeric labels are correctly assigned
    assert balanced_data['numeric_label'].tolist() == [1, 2, 1, 2]
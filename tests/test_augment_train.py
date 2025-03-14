import pytest
import pandas as pd
from src.augment_train import balance_dataset

# Mock data for testing
MOCK_DF = pd.DataFrame({
    'text': ['This is a positive sentence.', 'This is a negative sentence.'],
    'label': [1, 0]
})

# Mock augmenter for testing
class MockAugmenter:
    def augment(self, text):
        return f"augmented_{text}"

# Test balance_dataset with valid inputs
def test_balance_dataset_valid_inputs():
    """
    Test that the balance_dataset function balances the dataset correctly.
    """
    mock_augmenter = MockAugmenter()

    # Call the function
    balanced_df = balance_dataset(MOCK_DF, 'label', 'text', mock_augmenter)

    # Assertions
    assert isinstance(balanced_df, pd.DataFrame)
    assert len(balanced_df) == 4  # Original 2 rows + 2 augmented rows
    assert balanced_df['text'].str.startswith('augmented_').any()  # Check for augmented text
    assert balanced_df['label'].nunique() == 2  # Ensure both labels are present

# Test balance_dataset with empty DataFrame
def test_balance_dataset_empty_df():
    """
    Test that the balance_dataset function handles an empty DataFrame.
    """
    mock_augmenter = MockAugmenter()
    empty_df = pd.DataFrame(columns=['text', 'label'])

    # Call the function
    balanced_df = balance_dataset(empty_df, 'label', 'text', mock_augmenter)

    # Assertions
    assert isinstance(balanced_df, pd.DataFrame)
    assert len(balanced_df) == 0  # No rows should be added

# Test balance_dataset with single-class DataFrame
def test_balance_dataset_single_class():
    """
    Test that the balance_dataset function handles a DataFrame with only one class.
    """
    mock_augmenter = MockAugmenter()
    single_class_df = pd.DataFrame({
        'text': ['This is a positive sentence.', 'This is another positive sentence.'],
        'label': [1, 1]
    })

    # Call the function
    balanced_df = balance_dataset(single_class_df, 'label', 'text', mock_augmenter)

    # Assertions
    assert isinstance(balanced_df, pd.DataFrame)
    assert len(balanced_df) == 2  # No rows should be added
    assert balanced_df['label'].nunique() == 1  # Only one class should be present

# Test balance_dataset with invalid column names
def test_balance_dataset_invalid_columns():
    """
    Test that the balance_dataset function raises an error for invalid column names.
    """
    mock_augmenter = MockAugmenter()

    # Call the function with invalid column names
    with pytest.raises(KeyError):
        balance_dataset(MOCK_DF, 'invalid_label', 'invalid_text', mock_augmenter)

# Test balance_dataset with augmenter that returns None
def test_balance_dataset_augmenter_returns_none():
    """
    Test that the balance_dataset function handles an augmenter that returns None.
    """
    class MockAugmenterNone:
        def augment(self, text):
            return None

    mock_augmenter = MockAugmenterNone()

    # Call the function
    balanced_df = balance_dataset(MOCK_DF, 'label', 'text', mock_augmenter)

    # Assertions
    assert isinstance(balanced_df, pd.DataFrame)
    assert len(balanced_df) == 2  # No rows should be added
    assert balanced_df['text'].isnull().sum() == 0  # No None values should be present

# Test balance_dataset with augmenter that raises an exception
def test_balance_dataset_augmenter_raises_exception():
    """
    Test that the balance_dataset function handles an augmenter that raises an exception.
    """
    class MockAugmenterException:
        def augment(self, text):
            raise Exception("Augmentation failed")

    mock_augmenter = MockAugmenterException()

    # Call the function and check for exceptions
    with pytest.raises(Exception):
        balance_dataset(MOCK_DF, 'label', 'text', mock_augmenter)
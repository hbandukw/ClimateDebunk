import pytest
from pytest_mock import mocker
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch
from sklearn.metrics import precision_recall_curve, roc_curve, f1_score, auc
from src.utils import (
    plot_precision_recall, 
    plot_roc_curve, 
    calculate_f1_score, 
    plot_loss, 
    plot_accuracy, 
    plot_confusion_matrix
)

# Test 1: Test the plot_loss function. 
def test_plot_loss(mocker):
    # Mock plt.show() to prevent displaying the plot
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test data
    train_losses = [0.5, 0.4, 0.3]
    val_losses = [0.6, 0.5, 0.4]
    epochs = 3

    # Call the function
    plot_loss(train_losses, val_losses, epochs)

    # Assert that plt.show() was called
    mock_show.assert_called_once()

# Test 2: Test the plot_accuracy function.
def test_plot_accuracy(mocker):
    # Mock plt.show() to prevent displaying the plot
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test data
    train_accuracies = [0.8, 0.85, 0.9]
    val_accuracies = [0.75, 0.8, 0.85]
    epochs = 3

    # Call the function
    plot_accuracy(train_accuracies, val_accuracies, epochs)

    # Assert that plt.show() was called
    mock_show.assert_called_once()

# Test 3: Test the plot_confusion_matrix function.
def test_plot_confusion_matrix(mocker):
    # Mock plt.show() to prevent displaying the plot
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test data
    true_labels = [0, 1, 0, 1]
    pred_labels = [0, 1, 1, 0]
    classes = ['Class 0', 'Class 1']

    # Call the function
    plot_confusion_matrix(true_labels, pred_labels, classes)

    # Assert that plt.show() was called
    mock_show.assert_called_once()

# Test 4: Test the plot_precision_recall function.
def test_plot_precision_recall(mocker):
    # Mock plt.show() to prevent displaying the plot
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test data
    true_labels = [0, 1, 0, 1]
    pred_probs = [0.1, 0.9, 0.4, 0.6]

    # Call the function
    plot_precision_recall(true_labels, pred_probs)

    # Assert that plt.show() was called
    mock_show.assert_called_once()

# Test 5: Test the plot_roc_curve function.
def test_plot_roc_curve(mocker):
    # Mock plt.show() to prevent displaying the plot
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test data
    true_labels = [0, 1, 0, 1]
    pred_probs = [0.1, 0.9, 0.4, 0.6]

    # Call the function
    plot_roc_curve(true_labels, pred_probs)

    # Assert that plt.show() was called
    mock_show.assert_called_once()

# Test 6: Test the calculate_f1_score function.
def test_calculate_f1_score():
    # Test data
    true_labels = [0, 1, 0, 1]
    pred_labels = [0, 1, 1, 0]

    # Call the function
    f1 = calculate_f1_score(true_labels, pred_labels)

    # Assert the expected F1 score
    expected_f1 = f1_score(true_labels, pred_labels, average='weighted')
    assert f1 == expected_f1

# Test 7: Test plot_loss with invalid inputs.
def test_plot_loss_invalid_inputs(mocker):
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test empty inputs
    with pytest.raises(ValueError):
        plot_loss([], [], epochs=0)

    # Test mismatched lengths
    with pytest.raises(ValueError):
        plot_loss([0.5, 0.4], [0.6], epochs=2)

    # Test invalid epochs
    with pytest.raises(ValueError):
        plot_loss([0.5, 0.4], [0.6, 0.5], epochs=1)  # epochs < len(train_losses)

# Test 8: Test plot_accuracy with invalid inputs.
def test_plot_accuracy_invalid_inputs(mocker):
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test empty inputs
    with pytest.raises(ValueError):
        plot_accuracy([], [], epochs=0)

    # Test mismatched lengths
    with pytest.raises(ValueError):
        plot_accuracy([0.8, 0.85], [0.75], epochs=2)

    # Test invalid epochs
    with pytest.raises(ValueError):
        plot_accuracy([0.8, 0.85], [0.75, 0.8], epochs=1)  # epochs < len(train_accuracies)

# Test 9: Test plot_confusion_matrix with invalid inputs.
def test_plot_confusion_matrix_invalid_inputs(mocker):
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test empty inputs
    with pytest.raises(ValueError):
        plot_confusion_matrix([], [], classes=['Class 0', 'Class 1'])

    # Test mismatched lengths
    with pytest.raises(ValueError):
        plot_confusion_matrix([0, 1], [0], classes=['Class 0', 'Class 1'])

    # Test invalid classes
    with pytest.raises(ValueError):
        plot_confusion_matrix([0, 1], [0, 1], classes=[])  # Empty classes

# Test 10: Test plot_precision_recall with invalid inputs.
def test_plot_precision_recall_invalid_inputs(mocker):
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test empty inputs
    with pytest.raises(ValueError):
        plot_precision_recall([], [])

    # Test mismatched lengths
    with pytest.raises(ValueError):
        plot_precision_recall([0, 1], [0.1])

    # Test invalid probabilities
    with pytest.raises(ValueError):
        plot_precision_recall([0, 1], [1.1, -0.1])  # pred_probs outside [0, 1]

# Test 11: Test plot_roc_curve with invalid inputs.
def test_plot_roc_curve_invalid_inputs(mocker):
    mock_show = mocker.patch('matplotlib.pyplot.show')

    # Test empty inputs
    with pytest.raises(ValueError):
        plot_roc_curve([], [])

    # Test mismatched lengths
    with pytest.raises(ValueError):
        plot_roc_curve([0, 1], [0.1])

    # Test invalid probabilities
    with pytest.raises(ValueError):
        plot_roc_curve([0, 1], [1.1, -0.1])  # pred_probs outside [0, 1]

# Test 12: Test calculate_f1_score with invalid inputs.
def test_calculate_f1_score_invalid_inputs():
    # Test empty inputs
    with pytest.raises(ValueError):
        calculate_f1_score([], [])

    # Test mismatched lengths
    with pytest.raises(ValueError):
        calculate_f1_score([0, 1], [0])

    # Test invalid labels
    with pytest.raises(ValueError):
        calculate_f1_score([0, 1], [2, 3])  # pred_labels not in true_labels
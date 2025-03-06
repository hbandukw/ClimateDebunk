import pytest
import matplotlib.pyplot as plt
from unittest.mock import patch
from src.utils import plot_precision_recall, plot_roc_curve, calculate_f1_score
from sklearn.metrics import precision_recall_curve, roc_curve, f1_score, auc

# Sample data for testing
true_labels = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
pred_probs = [0.1, 0.9, 0.8, 0.2, 0.7, 0.3, 0.4, 0.6, 0.9, 0.1]
pred_labels = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]

@patch('src.utils.plt.show')
def test_plot_precision_recall(mock_show):
    plot_precision_recall(true_labels, pred_probs)
    precision, recall, _ = precision_recall_curve(true_labels, pred_probs)
    plt.plot.assert_called_with(recall, precision, marker='.')
    plt.xlabel.assert_called_with('Recall')
    plt.ylabel.assert_called_with('Precision')
    plt.title.assert_called_with('Precision-Recall Curve')
    mock_show.assert_called_once()

@patch('src.utils.plt.show')
def test_plot_roc_curve(mock_show):
    plot_roc_curve(true_labels, pred_probs)
    fpr, tpr, _ = roc_curve(true_labels, pred_probs)
    roc_auc = auc(fpr, tpr)
    plt.plot.assert_any_call(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot.assert_any_call([0, 1], [0, 1], 'k--')
    plt.xlabel.assert_called_with('False Positive Rate')
    plt.ylabel.assert_called_with('True Positive Rate')
    plt.title.assert_called_with('ROC Curve')
    plt.legend.assert_called_with(loc='lower right')
    mock_show.assert_called_once()

def test_calculate_f1_score():
    f1 = calculate_f1_score(true_labels, pred_labels)
    expected_f1 = f1_score(true_labels, pred_labels, average='weighted')
    assert f1 == expected_f1
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, f1_score, precision_recall_curve, roc_curve, auc

def plot_loss(train_losses, val_losses, epochs):
    """
    Plots the training and validation loss curves over epochs.

    Args:
        train_losses (list or array-like): List or array of training loss values for each epoch.
        val_losses (list or array-like): List or array of validation loss values for each epoch.
        epochs (int): The number of epochs.

    Returns:
        None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, epochs + 1), train_losses, label='Train Loss')
    plt.plot(range(1, epochs + 1), val_losses, label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Loss Curves')
    plt.legend()
    plt.show()

def plot_accuracy(train_accuracies, val_accuracies, epochs):
    """
    Plots the training and validation accuracy curves over epochs.

    Args:
        train_accuracies (list of float): List of training accuracies for each epoch.
        val_accuracies (list of float): List of validation accuracies for each epoch.
        epochs (int): Number of epochs.

    Returns:
        None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, epochs + 1), train_accuracies, label='Train Accuracy')
    plt.plot(range(1, epochs + 1), val_accuracies, label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Accuracy Curves')
    plt.legend()
    plt.show()

def plot_confusion_matrix(true_labels, pred_labels, classes):
    """
    Plots a confusion matrix using matplotlib.

    Parameters:
    true_labels (array-like): Array of true labels.
    pred_labels (array-like): Array of predicted labels.
    classes (list): List of class names corresponding to the labels.

    Returns:
    None
    """
    cm = confusion_matrix(true_labels, pred_labels)
    plt.figure(figsize=(10, 7))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

def plot_precision_recall(true_labels, pred_probs):
    """
    Plots the Precision-Recall curve for the given true labels and predicted probabilities.

    Args:
        true_labels (array-like): True binary labels.
        pred_probs (array-like): Predicted probabilities for the positive class.

    Returns:
        None
    """
    precision, recall, _ = precision_recall_curve(true_labels, pred_probs)
    plt.figure(figsize=(10, 5))
    plt.plot(recall, precision, marker='.')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.show()

def plot_roc_curve(true_labels, pred_probs):
    """
    Plots the Receiver Operating Characteristic (ROC) curve.

    Parameters:
    true_labels (array-like): True binary labels in range {0, 1} or {-1, 1}. If labels are not binary, pos_label should be explicitly given.
    pred_probs (array-like): Target scores, can either be probability estimates of the positive class, confidence values, or non-thresholded measure of decisions (as returned by decision_function on some classifiers).

    Returns:
    None: This function does not return anything. It displays the ROC curve plot.
    """
    fpr, tpr, _ = roc_curve(true_labels, pred_probs)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(10, 5))
    plt.plot(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.show()

def calculate_f1_score(true_labels, pred_labels):
    """
    Calculate the weighted F1 score for the given true and predicted labels.

    Parameters:
    true_labels (list or array-like): The ground truth labels.
    pred_labels (list or array-like): The predicted labels.

    Returns:
    float: The weighted F1 score.
    """
    return f1_score(true_labels, pred_labels, average='weighted')
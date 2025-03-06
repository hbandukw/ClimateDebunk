import torch
from torch.utils.data import DataLoader
from transformers import DistilBertTokenizer
import pandas as pd
from .model import load_model
from .data_prep import encode_data, QuotesDataset
from .utils import calculate_f1_score, plot_confusion_matrix, plot_precision_recall, plot_roc_curve
from . import config

def load_test_data(testpath: str):
    """Loads test data from the specified path."""
    if testpath.endswith(".csv"):
        test = pd.read_csv(testpath)
    elif testpath.endswith(".parquet"):
        test = pd.read_parquet(testpath)
    else:
        raise ValueError("Unsupported file type. Only CSV and Parquet are supported.")
    return test['quote'], test['numeric_label']



def test_model(model, test_loader, device):
    model.eval()
    test_loss = 0
    correct_test = 0
    total_test = 0
    all_test_labels = []
    all_test_preds = []
    with torch.no_grad():
        for batch in test_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            test_loss += outputs.loss.item()
            predictions = torch.argmax(outputs.logits, dim=-1)
            correct_test += (predictions == batch['labels']).sum().item()
            total_test += batch['labels'].size(0)
            all_test_labels.extend(batch['labels'].cpu().numpy())
            all_test_preds.extend(predictions.cpu().numpy())
    average_test_loss = test_loss / len(test_loader)
    accuracy = correct_test / total_test
    f1 = calculate_f1_score(all_test_labels, all_test_preds)
    return average_test_loss, accuracy, f1, all_test_labels, all_test_preds

def main():
    model = load_model()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    test_texts, test_labels = load_test_data(config["testpath"])
    tokenizer = DistilBertTokenizer.from_pretrained(config["tokenizer_model"], do_lower_case=True)
    test_dataset = encode_data(tokenizer, test_texts, test_labels, config["max_length"])
    test_loader = DataLoader(test_dataset, batch_size=config["batch_size"], shuffle=False)

    test_loss, test_accuracy, test_f1, test_labels, test_preds = test_model(model, test_loader, device)
    print(f"Test Loss: {test_loss}, Test Accuracy: {test_accuracy}, Test F1: {test_f1}")

    # Plot confusion matrix
    plot_confusion_matrix(test_labels, test_preds, classes=[str(i) for i in range(8)])

if __name__ == "__main__":
    main()
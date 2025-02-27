import torch


def validate_model(model, val_loader, device):
    model.eval()
    val_loss = 0
    correct_val = 0
    total_val = 0
    all_predictions = []
    all_true_labels = []
    with torch.no_grad():
        for batch in val_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            val_loss += outputs.loss.item()
            predictions = torch.argmax(outputs.logits, dim=-1)
            all_predictions.extend(predictions.cpu().numpy())
            all_true_labels.extend(batch['labels'].cpu().numpy())
            correct_val += (predictions == batch['labels']).sum().item()
            total_val += batch['labels'].size(0)
    average_val_loss = val_loss / len(val_loader)
    accuracy = correct_val / total_val
    return average_val_loss, accuracy, all_predictions, all_true_labels
import torch


def train_one_epoch(model, train_loader, optimizer, device):
    model.train()
    train_loss = 0
    correct_train = 0
    total_train = 0
    for batch in train_loader:
        optimizer.zero_grad()
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        predictions = torch.argmax(outputs.logits, dim=-1)
        correct_train += (predictions == batch['labels']).sum().item()
        total_train += batch['labels'].size(0)
    average_loss = train_loss / len(train_loader)
    accuracy = correct_train / total_train
    return average_loss, accuracy
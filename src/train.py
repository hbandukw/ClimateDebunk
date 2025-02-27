import torch
from torch.optim import AdamW, lr_scheduler
import yaml
import argparse

from src.model import 

# Load configuration
def load_config(config_path="configs/config.yaml"):
    """Loads YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    
    optimizer = AdamW(model.parameters(), lr= learning_rate)
    scheduler = lr_scheduler.StepLR(optimizer, step_size= step_size, gamma= gamma)


if __name__ == "__main__":
    main()
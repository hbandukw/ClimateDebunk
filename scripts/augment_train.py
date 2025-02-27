# Script used to create the augmented dataset: https://www.kaggle.com/datasets/rafechang/balancedfull
# Usage: python scripts/augment_data.py


import os
import re
import yaml
import argparse
import torch
import logging
import pandas as pd
import nlpaug.augmenter.word as naw
from sklearn.model_selection import KFold

# Load configuration
def load_config(config_path="configs/augmentation_config.yaml"):
    """Loads YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def extract_number(label):
    """Extracts the leading numeric label from a string."""
    match = re.match(r"(\d+)_", label)
    return int(match.group(1)) if match else None

# Setup logging
def setup_logging(log_level, save_to_file, log_file_path):
    """Configures logging settings."""
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), "INFO"),
        format=log_format,
        handlers=[logging.FileHandler(log_file_path)] if save_to_file else [logging.StreamHandler()]
    )

def balance_dataset(df, label_column, text_column, augmenter):
    """
    Augments underrepresented classes in a dataset to balance class distribution.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        label_column (str): Name of the column containing class labels.
        text_column (str): Name of the column containing text to augment.
        augmenter: NLP augmentation object with an 'augment' method.

    Returns:
        pd.DataFrame: A DataFrame with balanced class distribution.
    """
    class_counts = df[label_column].value_counts()
    max_count = class_counts.max()

    augmented_rows = []
    for label, deficit in (max_count - class_counts).items():
        if deficit > 0:
            sample_rows = df[df[label_column] == label].sample(n=deficit, replace=True)
            for _, row in sample_rows.iterrows():
                augmented_text = augmenter.augment(row[text_column])
                augmented_rows.append([augmented_text, label] + row.drop([text_column, label_column]).tolist())

    augmented_df = pd.DataFrame(augmented_rows, columns=[text_column, label_column] + 
                                [col for col in df.columns if col not in [text_column, label_column]])

    # Clean up augmented text formatting
    augmented_df[text_column] = augmented_df[text_column].astype(str).str.replace(r"^\['|'\]$", "", regex=True)
    balanced_df = pd.concat([df, augmented_df], ignore_index=True)
    balanced_df['label_column'] = balanced_df['label_column'].astype(int)

    return balanced_df

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Augments underrepresented classes in a dataset to balance class distribution")
    parser.add_argument("--config", type=str, default="configs/augmentation_config.yaml", help="Path to the configuration file.")
    args = parser.parse_args()
    
    # Load config
    config = load_config(args.config)

    # Setup logging
    setup_logging(config["log_level"], config["save_logs_to_file"], config["log_file_path"])
    
    logging.info("Loading dataset from: %s", config["data_path"])
    df = pd.read_parquet(config["data_path"])

    # Extract numeric labels
    df["numeric_label"] = df["label"].apply(extract_number)

    # Set device
    device = config["device"] if config["device"] in ["cuda", "cpu"] else ("cuda" if torch.cuda.is_available() else "cpu")
    logging.info("Using device: %s", device)

    # Define augmentation model
    augmenter = naw.ContextualWordEmbsAug(
        model_path=config["augmenter_model"],
        action=config["augment_action"],
        device=device
    )

    # Create output directory
    os.makedirs(config["output_dir"], exist_ok=True)

    # K-Fold splitting & augmentation
    kf = KFold(n_splits=config["n_splits"], shuffle=True, random_state=config["random_seed"])
    
    for i, (_, test_index) in enumerate(kf.split(df), start=1):
        subset = df.iloc[test_index]
        balanced_subset = balance_dataset(subset, "numeric_label", "quote", augmenter)

        subset_path = os.path.join(config["output_dir"], f"df{i}.csv")
        balanced_path = os.path.join(config["output_dir"], f"df_balanced{i}.csv")

        subset.to_csv(subset_path, index=False)
        balanced_subset.to_csv(balanced_path, index=False)

        logging.info("Saved: %s & %s", subset_path, balanced_path)

    if config["save_intermediate_splits"]:
        logging.info("Intermediate KFold splits saved.")
    
    

if __name__ == "__main__":
    main()
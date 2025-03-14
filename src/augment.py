import re
import pandas as pd
from sklearn.model_selection import KFold


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
import torch
import numpy as np
import pandas as pd
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer, AutoConfig
from torch.utils.data import DataLoader, Dataset
from onnxruntime.quantization import quantize_dynamic, QuantType, CalibrationDataReader
from utils import calculate_f1_score


def convert_to_onnx(model, config, quantize_config):
    """
    Converts a given PyTorch model to ONNX format.

    Args:
        model (torch.nn.Module): The PyTorch model to be converted.
        config (dict): Configuration dictionary containing tokenizer name and max length.
            - tokenizer_name (str): The name of the tokenizer to be used.
            - max_length (int): The maximum length for tokenization.
        quantize_config (dict): Configuration dictionary for ONNX export.
            - onnx_path (str): The file path where the ONNX model will be saved.

    Returns:
        None

    Example:
        config = {
            'tokenizer_name': 'distilbert-base-uncased',
            'max_length': 128
        }
        quantize_config = {
            'onnx_path': 'model.onnx'
        }
        convert_to_onnx(model, config, quantize_config)
    """
    tokenizer = DistilBertTokenizer.from_pretrained(config['tokenizer_name'])
    dummy_text = "This is a dummy input for ONNX conversion."
    dummy_inputs = tokenizer(dummy_text, return_tensors="pt", max_length=config['max_length'], padding="max_length", truncation=True)


    torch.onnx.export(
        model, 
        (dummy_inputs["input_ids"], dummy_inputs["attention_mask"]),
        quantize_config['onnx_path'],
        input_names=["input_ids", "attention_mask"],
        output_names=["logits"],
        dynamic_axes={"input_ids": {0: "batch_size"}, "attention_mask": {0: "batch_size"}},
        opset_version=14
    )
    print(f"Model exported to {quantize_config['onnx_path']}")


def dynamic_quantize(quantize_config):
    """
    Perform dynamic quantization on an ONNX model.

    Args:
        quantize_config (dict): A dictionary containing the following keys:
            - 'onnx_path' (str): The file path to the input ONNX model.
            - 'quantized_onnx_path' (str): The file path where the quantized ONNX model will be saved.

    Returns:
        None

    Notes:
        Saves the quantized ONNX model to the specified output path and prints a confirmation message.
    """
    quantize_dynamic(
        model_input=quantize_config['onnx_path'],
        model_output=quantize_config['quantized_onnx_path'],
        weight_type=QuantType.QInt8
    )
    print(f"Dynamic quantized model saved at {quantize_config['quantized_onnx_path']}")

    
def evaluate_onnx_model(session, val_loader):
    """
    Evaluate an ONNX model using a validation data loader.

    Args:
        session (onnxruntime.InferenceSession): The ONNX runtime session for the model.
        val_loader (DataLoader): A data loader providing validation data batches.
        
    Returns:
        tuple: A tuple containing:
            - accuracy (float): The accuracy of the model on the validation set.
            - f1 (float): The F1 score of the model on the validation set.
            - all_val_labels (list): A list of all true labels from the validation set.
            - all_val_preds (list): A list of all predicted labels from the validation set.
    """
    print("Starting ONNX evaluation...")
    total_correct = 0
    total_samples = 0
    all_val_labels = []
    all_val_preds = []

    for batch_idx, batch in enumerate(val_loader):
        print(f"Processing batch {batch_idx+1}...")
        # Ensure inputs are numpy arrays
        input_ids = np.array(batch["input_ids"], dtype=np.int64)
        attention_mask = np.array(batch["attention_mask"], dtype=np.int64)
        labels = np.array(batch["labels"], dtype=np.int64)

        # Prepare ONNX input dictionary
        inputs = {
            "input_ids": input_ids,
            "attention_mask": attention_mask
        }
        
        # Run inference
        outputs = session.run(["logits"], inputs)
        predictions = np.argmax(outputs[0], axis=1)

        # Compute accuracy
        batch_correct = np.sum(predictions == labels)
        total_correct += batch_correct
        total_samples += len(labels)
        all_val_labels.extend(labels)
        all_val_preds.extend(predictions)
        print(f"Batch {batch_idx+1}: {batch_correct}/{len(labels)} correct")

    accuracy = total_correct / total_samples
    f1 = calculate_f1_score(all_val_labels, all_val_preds)
    print(f"ONNX Validation Accuracy: {accuracy:.4f} ({total_correct}/{total_samples})")
    print(f"ONNX Validation F1 Score: {f1:.4f}")
    return accuracy, f1, all_val_labels, all_val_preds
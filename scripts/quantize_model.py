import yaml
import torch
import numpy as np
import onnx
import onnxruntime
from onnxruntime.quantization import quantize_dynamic, QuantType
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer, AutoConfig
from ..src.model import load_model
from ..src.data_prep import create_data_loader
from ..src.utils import plot_loss, plot_accuracy, calculate_f1_score


# Function to load config
def load_config(config_path):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def convert_to_onnx(onnx_path, model):
    """
    Convert a PyTorch model to ONNX format.

    Args:
        onnx_path (str): Path to save the ONNX model.
    """
    dummy_input = {
        "input_ids": torch.randint(0, 30522, (1, 365)),  # Random token IDs
        "attention_mask": torch.ones((1, 365))  # Full attention mask
    }

    torch.onnx.export(
        model,
        (dummy_input["input_ids"], dummy_input["attention_mask"]),
        onnx_path,
        input_names=["input_ids", "attention_mask"],
        output_names=["logits"],
        dynamic_axes={"input_ids": {0: "batch_size"}, "attention_mask": {0: "batch_size"}},
        opset_version=14  # ONNX opset for transformers
    )
    return 

def validate_onnx_model(session, val_loader):
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
    return accuracy, f1


def apply_dynamic_quant(onnx_path, quantized_onnx_path):
    """
    Apply dynamic quantization to the ONNX model.

    Args:
        onnx_path (str): Path to the input ONNX model.
        quantized_onnx_path (str): Path to save the quantized ONNX model.
    """
    quantize_dynamic(
        model_input=onnx_path,
        model_output=quantized_onnx_path,
        weight_type=QuantType.QInt8  # Quantizes weights to int8
    )

# Main function
def main():
    # Load Configs
    main_config = load_config('configs/config.yaml')
    quant_config = load_config('configs/quantization_config.yaml')

    # Load Fine-tuned Model
    model = load_model()
    model.load_state_dict(torch.load(main_config["trained_model_path"], map_location=torch.device("cpu")))
    model.eval()

    # Convert to ONNX
    convert_to_onnx(model, quant_config['onnx_path'])

    # Dynamic Quantization
    apply_dynamic_quant(quant_config['onnx_path'], quant_config['quantized_onnx_path'])

    # Load Validation Data
    val_loader = create_data_loader(
        filepath=main_config["validation_data_path"],
        label_column=main_config["label_column"],
        tokenizer_model=main_config["tokenizer_model"],
        max_length=main_config["max_length"],
        batch_size=main_config["batch_size"],
        shuffle=False
    )

    # Load ONNX Model
    session = onnxruntime.InferenceSession(quant_config['quantized_onnx_path'])

    # Validate ONNX Model
    validate_onnx_model(session, val_loader)

if __name__ == "__main__":
    main()

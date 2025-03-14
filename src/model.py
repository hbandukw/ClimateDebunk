import torch
from transformers import DistilBertConfig, DistilBertForSequenceClassification

def load_model_for_finetuning(config):
    """
    Loads and configures a DistilBERT model for sequence classification using parameters specified in a YAML config file.
    The function initializes the model with a pre-trained DistilBERT checkpoint, freezes all layers, unfreezes a specified number
    of transformer layers, and unfreezes the classifier layer for fine-tuning.
    Args:
        config (dict): A dictionary containing the model configuration with the following keys:
            - 'model_name' (str): The name of the pre-trained DistilBERT model to load (e.g., 'distilbert-base-uncased')
            - 'num_labels' (int): The number of output labels for the classification task.
            - 'dropout_rate' (float): The dropout rate applied to the model's layers for regularization. 
            - 'total_layers' (int): The total number of layers in the DistilBERT model (typically 6).
            - 'num_trainable_layers' (int): The number of transformer layers to unfreeze for fine-tuning. 
    Returns:
        DistilBertForSequenceClassification: The configured DistilBERT model ready for training or evaluation.

    Example:
        If the YAML configuration file contains:
        ```
        model_name: distilbert-base-uncased
        num_labels: 2
        dropout_rate: 0.1
        total_layers: 6
        num_trainable_layers: 2
        ```
        The function will:
        1. Load the 'distilbert-base-uncased' model with 2 output labels and a dropout rate of 0.1.
        2. Freeze all layers.
        3. Unfreeze the last 2 transformer layers (layers 5 and 6).
        4. Unfreeze the classifier layer.

    """
    model_config = DistilBertConfig.from_pretrained(
        config['model_name'],
        num_labels=config['num_labels'],
        dropout=config['dropout_rate'],
        attention_dropout=config['dropout_rate']
    )
   
    model = DistilBertForSequenceClassification.from_pretrained(config['model_name'],
                                                                 config=model_config)
    
    # Freeze all layers
    for name, param in model.named_parameters():
        param.requires_grad = False

    # Unfreeze the specified number of layers
    for layer_idx in range(config['total_layers'] - config['num_trainable_layers'], config['total_layers']):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            param.requires_grad = True

    # Unfreeze the classifier layer
    for name, param in model.classifier.named_parameters():
        param.requires_grad = True

    return model


def load_model_for_inference(config, device):
    """
    Loads a pre-trained DistilBERT model for inference, using configuration parameters specified in a YAML file.
    The function initializes the model, loads trained weights, freezes all layers to prevent gradient computation,,
    and sets the model to evaluation mode.

    Args:
        config (dict): A dictionary containing the model configuration, typically loaded from a YAML file. Expected keys include:
            - 'model_name' (str): The name or path of the pre-trained DistilBERT model (e.g., 'distilbert-base-uncased').
            - 'num_labels' (int): The number of output labels for the classification task.
            - 'trained_model_path' (str): The file path to the trained model weights (e.g., a `.pt` or `.bin` file).
        device (str or torch.device): The device to load the model onto (e.g., 'cpu' or 'cuda').

    Returns:
        DistilBertForSequenceClassification: The trained DistilBERT model, loaded with trained weights, frozen, and set to evaluation mode.

    Example:
        If the YAML configuration file contains:
        ```
        model_name: distilbert-base-uncased
        num_labels: 2
        trained_model_path: /path/to/trained_model.pt
        ```
        And the device is set to 'cpu', the function will:
        1. Load the 'distilbert-base-uncased' model with 2 output labels.
        2. Load the trained weights from `/path/to/trained_model.pt`.
        3. Freeze all layers to prevent gradient computation.
        4. Set the model to evaluation mode.
    
    """
    
    # Load model configuration
    model_config = DistilBertConfig.from_pretrained(
        config['model_name'],
        num_labels=config['num_labels']
    )

    # Initialize model
    model = DistilBertForSequenceClassification.from_pretrained(config['model_name'],
                                                             config=model_config)

    # Load trained weights
    model.load_state_dict(torch.load(config['trained_model_path'],
                                    map_location=torch.device(device)))  

    # Freeze all layers 
    for param in model.parameters():
        param.requires_grad = False

    # Set the model to evaluation mode
    model.eval()

    return model



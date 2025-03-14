import torch
from transformers import DistilBertConfig, DistilBertForSequenceClassification

def load_model(config):
    """Loads and returns the DistilBERT model with the specified configuration."""
    model_config = DistilBertConfig.from_pretrained(
        config['model_name'],
        num_labels=config['num_labels'],
        dropout=config['dropout_rate'],
        attention_dropout=config['dropout_rate']
    )
   
    model = DistilBertForSequenceClassification.from_pretrained(config['model_name'], config=model_config)
    
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
    """Loads and returns the DistilBERT model for inference with trained weights."""
    
    # Load model configuration
    model_config = DistilBertConfig.from_pretrained(
        config['model_name'],
        num_labels=config['num_labels']
    )

    # Initialize model
    model = DistilBertForSequenceClassification.from_pretrained(config['model_name'], config=model_config)

    # Load trained weights
    model.load_state_dict(torch.load(config['trained_model_path'], map_location=torch.device(device)))  

    # Freeze all layers to avoid unnecessary computation
    for param in model.parameters():
        param.requires_grad = False

    # Set the model to evaluation mode
    model.eval()

    return model



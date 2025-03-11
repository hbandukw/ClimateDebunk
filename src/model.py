from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, DistilBertConfig
import torch
from . import config

def load_model():
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
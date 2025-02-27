def setup_model_for_hyperopt(num_trainable_layers, dropout_rate):
    config = DistilBertConfig.from_pretrained(
        'distilbert-base-uncased',
        num_labels=8,
        dropout=dropout_rate,
        attention_dropout=dropout_rate
    )
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', config=config)
    for name, param in model.named_parameters():
        param.requires_grad = False
    for layer_idx in range(6 - num_trainable_layers, 6):
        for name, param in model.distilbert.transformer.layer[layer_idx].named_parameters():
            param.requires_grad = True
    for name, param in model.classifier.named_parameters():
        param.requires_grad = True
    return model
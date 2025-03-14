from huggingface_hub import HfApi

api = HfApi()

repo_id = "ClimateDebunk/Quantized_DistilBertForSequenceClassification"  
model_path = "distilbert_quantized_dynamic.onnx"

api.upload_file(
    path_or_fileobj=model_path,
    path_in_repo="model.onnx",
    repo_id=repo_id,
    repo_type="model"
)
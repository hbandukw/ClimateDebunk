from fastapi import APIRouter
from datetime import datetime
from datasets import load_dataset
from sklearn.metrics import accuracy_score
import random

from .utils.evaluation import TextEvaluationRequest
from .utils.emissions import tracker, clean_emissions_data, get_space_info

router = APIRouter()

DESCRIPTION = "Random Baseline"
ROUTE = "/text"

@router.post(ROUTE, tags=["Text Task"], 
             description=DESCRIPTION)
async def evaluate_text(request: TextEvaluationRequest):
    """
    Evaluate text classification for climate disinformation detection.
    
    Current Model: Random Baseline
    - Makes random predictions from the label space (0-7)
    - Used as a baseline for comparison
    """
    # Get space info
    username, space_url = get_space_info()

    # Define the label mapping
    LABEL_MAPPING = {
        "0_not_relevant": 0,
        "1_not_happening": 1,
        "2_not_human": 2,
        "3_not_bad": 3,
        "4_solutions_harmful_unnecessary": 4,
        "5_science_unreliable": 5,
        "6_proponents_biased": 6,
        "7_fossil_fuels_needed": 7
    }

    # Load and prepare the dataset
    dataset = load_dataset(request.dataset_name)

    # Convert string labels to integers
    dataset = dataset.map(lambda x: {"label": LABEL_MAPPING[x["label"]]})

    # Split dataset
    train_test = dataset["train"]
    test_dataset = dataset["test"]
    
    # Start tracking emissions
    tracker.start()
    tracker.start_task("inference")

    #--------------------------------------------------------------------------------------------
    # YOUR MODEL INFERENCE CODE HERE
    # Update the code below to replace the random baseline by your model inference within the inference pass where the energy consumption and emissions are tracked.
    #--------------------------------------------------------------------------------------------   
    
    # Make random predictions (placeholder for actual model inference)
    #true_labels = test_dataset["label"]
    #predictions = [random.randint(0, 7) for _ in range(len(true_labels))]

    from transformers import DistilBertTokenizer
    import numpy as np
    import onnxruntime as ort
    from huggingface_hub import hf_hub_download
    
    # Load the ONNX model and tokenizer
    MODEL_REPO = "ClimateDebunk/Quantized_DistilBertForSequenceClassification"
    MODEL_FILENAME = "distilbert_quantized_dynamic.onnx"
    MODEL_PATH = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILENAME)

    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    ort_session = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])

    # Preprocess the text data
    def preprocess(texts):
        return tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=365,
            return_tensors="np"
        )

    # Run inference
    def predict(texts):
        inputs = preprocess(texts)
        ort_inputs = {
            "input_ids": inputs["input_ids"].astype(np.int64),
            "attention_mask": inputs["attention_mask"].astype(np.int64)
        }
        ort_outputs = ort_session.run(None, ort_inputs)
        logits = ort_outputs[0]
        predictions = np.argmax(logits, axis=1)
        return predictions

     # Replace the random predictions with actual model predictions
    texts = test_dataset["quote"]
    predictions = predict(texts)

    true_labels = test_dataset["label"]

    #--------------------------------------------------------------------------------------------
    # YOUR MODEL INFERENCE STOPS HERE
    #--------------------------------------------------------------------------------------------   

    
    # Stop tracking emissions
    emissions_data = tracker.stop_task()
    
    # Calculate accuracy
    accuracy = accuracy_score(true_labels, predictions)
    
    # Prepare results dictionary
    results = {
        "username": username,
        "space_url": space_url,
        "submission_timestamp": datetime.now().isoformat(),
        "model_description": DESCRIPTION,
        "accuracy": float(accuracy),
        "energy_consumed_wh": emissions_data.energy_consumed * 1000,
        "emissions_gco2eq": emissions_data.emissions * 1000,
        "emissions_data": clean_emissions_data(emissions_data),
        "api_route": ROUTE,
        "dataset_config": {
            "dataset_name": request.dataset_name,
            "test_size": request.test_size,
            "test_seed": request.test_seed
        }
    }
    
    return results 
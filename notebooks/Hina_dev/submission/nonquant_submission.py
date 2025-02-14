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

    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    import torch
  
    # Load model and tokenizer from Hugging Face Hub
    MODEL_REPO = "ClimateDebunk/FineTunedDistilBert4SeqClass"

    tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased', do_lower_case=True)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_REPO)

    model.eval()  # Set to evaluation mode
    
    def preprocess(texts):
        """ Tokenize text inputs for DistilBERT """
        return tokenizer(texts, padding='max_length', truncation=True, max_length=365, return_tensors="pt")
    
    def predict(texts):
        """ Run inference using the fine-tuned DistilBERT model """
        inputs = preprocess(texts)
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=1).tolist()
        return predictions
    
    # Run inference
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
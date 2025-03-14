# ClimateDebunk

Authors: Hina Bandukwala, Rafe Chang

## Project Overview
This project is part of the HuggingFace Frugal AI Challenge where we are tasked with creating an efficient model for classifying quotes relating to climate change as one of 8 predefined categories based on the [CARDS taxonomy](http://cardsclimate.com/). 

### Data
The training data consists of ~6000 quotes from various sources. The quotes are labeled with one of the above mentioned 8 categories. More information about the data can be found [here](https://huggingface.co/datasets/QuotaClimat/frugalaichallenge-text-train). 

We augmented the training data using the `nlpaug` library to deal with the class imbalance in the original dataset. The augmented training data consists of ~12000 quotes.

The original training and validation datasets as well as the augmented data can be found [here](https://www.kaggle.com/datasets/hbandukw/hf-frugal-ai-datasets).

### Model
We used a pretrained [DistilBERT](https://huggingface.co/docs/transformers/v4.49.0/en/model_doc/distilbert#transformers.DistilBertForSequenceClassification) model for sequence classification and fine-tuned it using our augmented dataset. We incorporated a learning rate scheduler, applied regularization techniques, and performed hyperparameter tuning to improve the model's performance achieving an accuracy of 95% on the validation set. Given the high accuracy, we acknowledge that the model is overfitting on the training data.

## Repository Structure
```
ClimateDebunk/
├── configs/               # Configuration files
│   ├── augmentation_config.yaml
│   ├── config.yaml
│   ├── hyperoptim_config.yaml
│   └── quantization_config.yaml
├── data/                  # Data files
│   ├── test/              # Test data
│   ├── train/             # Training data
│   └── valid/             # Validation data
├── models/                # Trained models
├── notebooks/             # Jupyter notebooks
│   ├── 01_augment_train.ipynb
│   ├── 02_hyperoptimization.ipynb
│   ├── 03_train_model.ipynb
│   ├── 04_inference.ipynb
│   └── 05_quantization.ipynb
├── src/                   # Source code
│   ├── augment_train.py   # Data augmentation script
│   ├── config.py          # Configuration utilities
│   ├── data_prep.py       # Data preparation script
│   ├── hyperoptim.py      # Hyperparameter optimization script
│   ├── model.py           # Model definition
│   ├── quantize.py        # Model quantization script
│   ├── train.py           # Training script
│   └── utils.py           # Utility functions
├── tests/                 # Test files
│   ├── test_augment_train.py
│   ├── test_config.py
│   ├── test_data_prep.py
│   ├── test_hyperoptim.py
│   ├── test_model.py
│   ├── test_quantize.py
│   ├── test_train.py
│   └── test_utitls.py      
├── environment.yml        # Conda environment file
└── README.md              # Project documentation
```

## Set up
To set up the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ClimateDebunk.git
cd ClimateDebunk
```

2. Use the environment.yml file to set up a conda environment with all the required dependencies:

```bash
conda env create -f environment.yml
conda activate climate_debunk
```

3. Test

```bash 
pytest tests
```

## Usage

### Inference
The project is set up such that you can use the model for inference on your own data. To do so, follow these steps:

1. Populate configuration file

Fill in the required information in the `config.yaml` file:

```yaml
- testpath: "path/to/test/data"  # path to your test data
- test_label_col: "label"  # column name for label data
- trained_model_path: "path/to/trained/model"  # path to trained model
```

2. Run the inference notebook

This notebook can be found at `notebooks/04_inference.ipynb`. It will load the trained model and perform inference on the test data.

### Notes
We worked on quantizing the model to reduce its size and make it more efficient for deployment. However, we were unable to complete this task due to time constraints. The notebook for quantization can be found at `notebooks/05_quantization.ipynb`.
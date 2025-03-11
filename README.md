# ClimateDebunk

## Inference
# Step 1: Download the test data and add it to the repo in the data folder. 

# Step 2: Run the inference.py script to get predictions. 



#### Data 
Location: https://www.kaggle.com/datasets/hbandukw/hf-frugal-ai-datasets


Training set: train-00000-of-00001.parquet  # source: https://huggingface.co/datasets/QuotaClimat/frugalaichallenge-text-train
Validation set: test-00000-of-00001.parquet # source: https://huggingface.co/datasets/QuotaClimat/frugalaichallenge-text-train
Augmented and Balanced: aug_balanced_train.csv # created by augmented train-00000-of-00001.parquet using scripts/augment_train.py


## Scripts
- `augment_train.py`: Augment the training set using the `nlpaug` library. The script will create a new csv file with the augmented data. This data was used for hyperparameter tuning. 
- `hyperparameter_tuning.py`: Hyperparameter tuning using `optuna` library. The optimal hyperparameters can be found in the config file and used to train the model.
- `train.py`: Train the model using the optimal hyperparameters found in the hyperparameter tuning step. The model will be saved at the output path defined at trained_model_path in the config file. The pytorch model has been uploaded to Kaggle. 
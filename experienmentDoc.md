Here we document the experiements we've tried before compiling the final model. 

Data Augmentation: 
- We discovered an imbalance between classes. We suspect this caused model's poor performace, therefore employ data augmentation to create new data to achieve class balance. 
- Before using the test.parquet provided, we splitted 20% of the data as validation (no modification,) then augmented on the 80% of the data to use as training. 

Hyperparameter Optimization: 
- The accuracy of the fine-tuned disterbert model is low. 
- Instead of just fine-tuning, we decided to use optuna for hyperparameter optimization. Doing so will optimize the model's training process. 
- Besides the final hyperparameter used (`learning_rate`, `num_trainable_layers`, `dropout_rate`, `batch_size`, `epochs`, `step_size`, and `gamma`,) we also attempted with early stopping and fradient clipping. However, the model's accuracy decreased with these parameters included so we decided to not include these. 
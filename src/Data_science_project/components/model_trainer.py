import pandas as pd
import os
from src.Data_science_project import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.Data_science_project.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)  # Refer cells above for clarity
        lr.fit(train_x, train_y)  # Model Training

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))  #  Dumping the entire file in form of joblib
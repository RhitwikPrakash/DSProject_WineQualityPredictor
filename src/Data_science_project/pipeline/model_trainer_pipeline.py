from src.Data_science_project.config.configuration import ConfigurationManager
from src.Data_science_project.components.model_trainer import ModelTrainer
from src.Data_science_project import logger

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
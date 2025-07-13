from src.Data_science_project.config.configuration import ConfigurationManager
from src.Data_science_project.components.data_transformation import DataTransformation
from src.Data_science_project.utils.common import logger
from src.Data_science_project.constants import *

from pathlib import Path


STAGE_NAME="Data Trnasformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):   # Initiate the Data Transformation package

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":  # If Validation status is True, or Data Schema is valid
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:   # Data Schema is invalid
                raise Exception("Your data scheme is not valid")
            
        except Exception as e:
            print(e)
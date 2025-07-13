from src.Data_science_project.config.configuration import ConfigurationManager
from src.Data_science_project.components.data_ingestion import DataIngestion
from src.Data_science_project.utils.common import logger
from src.Data_science_project.constants import *

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline: 
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager(
        config_filepath="config/config.yaml",
        params_filepath="params.yaml",
        schema_filepath="schema.yaml"
        )
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



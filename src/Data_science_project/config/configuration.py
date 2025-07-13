from src.Data_science_project.constants import *
from src.Data_science_project.utils.common import read_yaml, create_directories
from src.Data_science_project.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig)
from pathlib import Path


class ConfigurationManager:
    def __init__(self, 
                 config_filepath= CONFIG_FILE_PATH,
                 params_filepath= PARAMS_FILE_PATH,
                 schema_filepath= SCHEMA_FILE_PATH):
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        self.schema = read_yaml(Path(schema_filepath))
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        print("✅ Created data_ingestion_config:", data_ingestion_config)
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=self.schema.COLUMNS  # ✅ ADD THIS LINE
    )
        print("✅ Created data_validation_config:", data_validation_config)
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )
        return data_transformation_config
    
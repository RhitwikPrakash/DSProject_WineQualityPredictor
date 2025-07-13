from dataclasses import dataclass
from pathlib import Path
from typing import Dict

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: str
    unzip_data_dir: str
    STATUS_FILE: str
    all_schema: dict  # ✅ Add this line

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    # In the initial stages, "params.yaml" file had only - key:value. Replace it with ElasticNet:  alpha: 0.2, l1_ratio: 0.1
    alpha: float   # Some parameters will be specified there, for ElasticNet ML Algorithm
    l1_ratio: float   
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    mlflow_uri: str
    all_params: Dict
    target_column: str
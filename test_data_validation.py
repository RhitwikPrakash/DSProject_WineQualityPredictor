from src.Data_science_project.config.configuration import ConfigurationManager
from src.Data_science_project.components.data_validation import DataValiadtion

try:
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValiadtion(config=data_validation_config)
    data_validation.validate_all_columns()
    print("✅ Data Validation Passed.")
except Exception as e:
    print("❌ Data Validation Failed:", e)

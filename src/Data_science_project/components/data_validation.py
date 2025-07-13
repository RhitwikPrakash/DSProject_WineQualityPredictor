class DataValiadtion:
    def __init__(self, config):
        self.config = config

    def validate_all_columns(self):
        import pandas as pd

        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            schema = self.config.all_schema

            # Check columns
            if set(schema.keys()) != set(data.columns):
                raise ValueError("Column names do not match schema.")

            # Check datatypes
            for col in data.columns:
                if data[col].dtype != schema[col]:
                    print(f"⚠️ Mismatch in {col}: Expected {schema[col]}, got {data[col].dtype}")

            with open(self.config.STATUS_FILE, "w") as f:
                f.write("Validation status: True")
            print("✅ Schema validation passed.")

        except Exception as e:
            with open(self.config.STATUS_FILE, "w") as f:
                f.write("Validation status: False")
            raise e

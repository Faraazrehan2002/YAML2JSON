import yaml
import json
from pathlib import Path

def load_yaml(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return {}

def transform_data(data: dict) -> dict:
    if 'metadata' in data and isinstance(data['metadata'], dict):
        for key, value in data['metadata'].items():
            data[f'metadata_{key}'] = value
        del data['metadata']
    return data

def save_json(data: dict, output_path: str):
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)
        print(f"JSON written to: {output_path}")

if __name__ == "__main__":
    input_yaml = "sample_config.yaml"
    output_json = "transformed_config.json"

    if not Path(input_yaml).exists():
        
        sample = {
            'service': 'payment',
            'version': '1.2',
            'metadata': {
                'created_by': 'admin',
                'env': 'prod'
            }
        }
        with open(input_yaml, 'w') as f:
            yaml.dump(sample, f)

    raw_data = load_yaml(input_yaml)
    transformed = transform_data(raw_data)
    save_json(transformed, output_json)

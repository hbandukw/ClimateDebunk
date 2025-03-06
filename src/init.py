import yaml

def load_config(config_path="configs/config.yaml"):
    """Loads YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
    
config = load_config()
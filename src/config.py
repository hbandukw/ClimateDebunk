import yaml

def load_config(config_path):
    """
    Loads a YAML configuration file from the specified path.

    Args:
        config_path (str): The path to the YAML configuration file.

    Returns:
        dict: The contents of the YAML file as a dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    """Loads YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

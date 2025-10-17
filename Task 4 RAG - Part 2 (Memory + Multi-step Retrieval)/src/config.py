import yaml

def load_config(path: str = "configs/settings.yaml") -> dict:
    """
    Load YAML configuration file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

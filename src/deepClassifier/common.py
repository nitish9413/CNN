import os
from box.exceptions import BoxValueError
import sys
import yaml
from deepClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox

@ensure_annotations
def read_config(config_path: str) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        config_path (str): path to the yaml file

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            config = ConfigBox(config)
            return config
    except BoxValueError as e:
        logger.error(f"Error in config file: {e}")
        sys.exit(1)
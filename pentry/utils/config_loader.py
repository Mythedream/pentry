#config_loader.py
from .logger import get_logger
import os
from typing import Optional
import yaml

logger = get_logger(__name__)

def load_folder_structure(template: str = "default", path: Optional[str] = None) -> list:
    """
    Loads a folder structure configuration from a YAML file.

    Args:
        template (str): The template name to retrieve from the configuration. Defaults to "default".
        path (str): The path to the YAML configuration file. Defaults to None, which uses the package's folders.yaml.

    Returns:
        list: The folder structure configuration for the specified template.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If there is an error parsing the YAML file.
    """
    result = []
    try:
        if path is None:
            path = os.path.join(os.path.dirname(__file__), "..", "config", "folders.yaml")
            path = os.path.abspath(path)
        logger.info(f"Loading folder structure from {path} using template '{template}'")
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
            if template in config:
                logger.debug(f"Template '{template}' found in configuration.")
                result = config[template]
                if not isinstance(result, list):
                    logger.warning(f"Template '{template}' is not a list. Returning empty list.")
                    result = []
            else:
                logger.warning(f"Template '{template}' not found in configuration. Returning empty list.")
    except FileNotFoundError:
        logger.error(f"Configuration file not found at {path}")
        raise FileNotFoundError(f"Configuration file not found at {path}")
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        raise ValueError(f"Error parsing YAML file: {e}")
    return result
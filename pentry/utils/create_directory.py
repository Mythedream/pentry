#utils.py

import os
from .logger import get_logger

logger = get_logger("pentry")

def create_directory(path: str, exist_ok: bool = True) -> str:
    """
    Create a directory at the given path.
    
    Args: 
        path (str): The path where the directory should be created.
        exist_ok (bool): If True, do not raise an error if the directory already exists.

    Returns:
        str: The absolute path of the created directory.
    """
    abs_path = os.path.abspath(os.path.expanduser(path))

    try: 
        os.makedirs(abs_path, exist_ok=exist_ok)
        logger.info(f"Directory created at: {abs_path}")
    except FileExistsError as e:
        logger.warning(f"Directory already exists: {abs_path}")
    except Exception as e:
        logger.error(f"Failed to create directory {abs_path}: {e}")
        raise

    return abs_path

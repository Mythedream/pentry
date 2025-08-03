import logging
import os
from datetime import datetime
from typing import Optional

# Cache to ensure the same log file is reused per logger name
_log_file_cache = {}

def get_logger(new_name: Optional[str] = None, log_dir: str = "logs", debug: bool = False) -> logging.Logger:
    """
    Returns a logger that logs to both console and file.

    Args:
        new_name (str): Name of the logger. Defaults to __name__.
        log_dir (str): Directory where log files will be stored.
        debug (bool): If True, sets log level to DEBUG; otherwise INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    new_name = new_name or __name__
    logger = logging.getLogger(name=new_name)

    if not logger.handlers:
        log_level = logging.DEBUG if debug else logging.INFO
        logger.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        os.makedirs(log_dir, exist_ok=True)

        # Reuse the same log file name per logger session
        if new_name not in _log_file_cache:
            _log_file_cache[new_name] = os.path.join(
                log_dir, f"{new_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
            )
        log_file = _log_file_cache[new_name]

        # Console Stream Handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)

        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

        logger.debug(f"Logger initialized for '{new_name}' with level {logging.getLevelName(log_level)}")

    return logger

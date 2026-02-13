from logging import Logger
from datetime import datetime
import logging
from configs.settings import LOGS_DIR, log_level

# get the log_level
LOG_LEVEL = log_level

# Define log format
LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'

def setup_logger(name: str, log_level: str=LOG_LEVEL) -> Logger:
    """
    Set up and configure a logger...
    
    Args:
        name: Logger name (e.g., 'extract', 'transform')
        log_level: Minimum log level (DEBUG, INFO, WARNING, ERROR)
    
    Returns:
        Configured Logger instance
    """
    logger = logging.getLogger(name)
    level = getattr(logging, log_level.upper())
    logger.setLevel(level)

    if logger.handlers:
        return logger
    
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime('%Y%m%d')
    log_file = LOGS_DIR / f'etl_{today}.log'
    error_file = LOGS_DIR / f'error_{today}.log'

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    error_handler = logging.FileHandler(error_file)
    error_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.addHandler(error_handler)

    return logger
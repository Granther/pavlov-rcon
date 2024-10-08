import os
import logging
from dotenv import load_dotenv

def create_logger(name) -> logging.Logger:
    """Returns instantiated logger using environment settings"""

    load_dotenv()

    logger = logging.getLogger(name)
    log_level = os.environ.get("LOG_LEVEL")
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(os.path.join(os.environ.get("LOGS_DIR"), f"{log_level}.log"))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

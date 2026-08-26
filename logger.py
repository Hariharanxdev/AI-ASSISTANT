import logging
import os


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "assistant.log")


def setup_logger():
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("AI_Assistant")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

        formatter = logging.Formatter(
            "%(asctime)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger()
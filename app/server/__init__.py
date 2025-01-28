import logging
import os
from pathlib import Path

Path("logs/info").mkdir(parents=True, exist_ok=True)
Path("logs/warnings").mkdir(parents=True, exist_ok=True)
Path("logs/errors").mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/info/info.log", mode="a"),
        logging.FileHandler("logs/warnings/warnings.log", mode="a"),
        logging.FileHandler("logs/errors/errors.log", mode="a"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
logger.info("Logger is set up and running.")

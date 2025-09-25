from app.core.settings.config import get_settings, Settings
import logging
import os
from pathlib import Path

settings: Settings = get_settings()


async def set_up_logs():
    log_dir = Path(settings.BASE_DIRECTORY, "logs")
    (log_dir / "info").mkdir(parents=True, exist_ok=True)
    (log_dir / "warnings").mkdir(parents=True, exist_ok=True)
    (log_dir / "errors").mkdir(parents=True, exist_ok=True)

    info_handler = logging.FileHandler(log_dir / "info" / "info.log", mode="a")
    warnings_handler = logging.FileHandler(log_dir / "warnings" / "warnings.log", mode="a")
    errors_handler = logging.FileHandler(log_dir / "errors" / "errors.log", mode="a")
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
    )
    for handler in (info_handler, warnings_handler, errors_handler, console_handler):
        handler.setFormatter(formatter)

    # Add filters so each file only gets its level
    class LevelFilter(logging.Filter):
        def __init__(self, level):
            super().__init__()
            self.level = level

        def filter(self, record: logging.LogRecord) -> bool:
            if self.level == logging.INFO:
                return record.levelno == logging.INFO
            if self.level == logging.WARNING:
                return record.levelno == logging.WARNING
            if self.level == logging.ERROR:
                return record.levelno >= logging.ERROR
            return False

    info_handler.addFilter(LevelFilter(logging.INFO))
    warnings_handler.addFilter(LevelFilter(logging.WARNING))
    errors_handler.addFilter(LevelFilter(logging.ERROR))

    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        handlers=[info_handler, warnings_handler, errors_handler, console_handler],
    )

    logger = logging.getLogger(__name__)
    logger.info("Logger is set up and running.")

import logging
from logging.handlers import RotatingFileHandler
from time import sleep

from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, track

console_handler = RichHandler(level=logging.INFO, rich_tracebacks=True, show_path=False)

logging.basicConfig(level=logging.DEBUG, format="%(message)s", handlers=[console_handler])
logging.getLogger("matplotlib").setLevel(logging.WARNING)
logging.captureWarnings(True)


def add_file_handler(logger, filename="app.log", max_bytes=10_000_000, backup_count=3):
    file_handler = RotatingFileHandler(filename, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)s:%(lineno)d | %(message)s"))
    logger.addHandler(file_handler)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.info("Processing %d snapshots", 128)
    logger.debug("Solver tolerance: %.2e", 1e-8)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception("Calculation failed")
    array = range(3)  # Example array for demonstration purposes

    for item in track(array):
        sleep(0.3)

    with Progress(SpinnerColumn(), *Progress.get_default_columns()) as progress:
        for item in progress.track(array, description="Processing"):
            sleep(0.3)

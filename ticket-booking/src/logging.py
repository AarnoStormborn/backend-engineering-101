import sys
from loguru import logger

LOG_FORMAT = "{time:DD-MM-YYYY HH:mm:ss} > {level}\t| {file}\t| {message}"

logger.remove()

# stdout
logger.add(
    sys.stdout, level="INFO", colorize=True,
    format=LOG_FORMAT,
    filter=lambda record: record["level"].name in ("INFO", "WARNING")
)
# stderr
logger.add(
    sys.stderr, level="ERROR", colorize=True,
    format=LOG_FORMAT,
    filter=lambda record: record["level"].name in ("ERROR", "CRITICAL")
)

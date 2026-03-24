import sys
from loguru import logger

def setup_logger():
    # Remove default handler to avoid duplicate logs
    logger.remove()

    # Console sink
    logger.add(sys.stdout,
               level="INFO")

    # File sink with rotation and retention
    logger.add("logs/app.log",
               rotation="10 MB",       # new file after 10 MB
               retention="7 days",     # keep logs for 7 days
               compression="zip",      # compress old logs
               level="DEBUG",
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}")

    return logger

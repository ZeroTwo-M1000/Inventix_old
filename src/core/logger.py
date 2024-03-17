from loguru import logger

logger.remove()
logger.add(
    sink="../../logs/logs-info.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | <level>{level}</level> | <level>{message}</level>",
    level="INFO",
    rotation="10MB",
    compression="zip",
    filter=lambda record: record["level"].name == "INFO",
)

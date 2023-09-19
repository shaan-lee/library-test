import logging
from get_logger import get_logger


logger = get_logger("test_logger", "info")
logging.basicConfig(level="DEBUG")

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
logger.error(__file__)

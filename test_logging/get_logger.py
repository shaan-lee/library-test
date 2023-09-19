import logging


logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
)


def get_logger(name, level="WARNING"):
    logger = logging.getLogger(name)
    logger.setLevel(level.upper())
    return logger

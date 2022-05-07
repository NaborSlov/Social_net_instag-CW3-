import logging


def create_logger():
    logger = logging.getLogger("basik")
    logger.setLevel("INFO")

    file_handler = logging.FileHandler("logs/basik.log", encoding='UTF-8')
    formatter = logging.Formatter("%(levelname)s %(asctime)s : %(message)s  %(pathname)s >> %(funcName)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

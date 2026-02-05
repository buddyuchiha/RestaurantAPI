import logging 

from app.core.settings import settings


logger = logging.Logger("RestaurantAPI logger")
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)


file_handler = logging.FileHandler(settings.APP_LOGGING_FILE)
file_handler.setFormatter(formatter)
file_handler.setLevel("INFO")


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel("ERROR")


logger.addHandler(file_handler)
logger.addHandler(stream_handler)
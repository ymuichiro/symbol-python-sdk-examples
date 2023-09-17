from dotenv import load_dotenv
import logging
import os


load_dotenv()
PRIVATE_KEY: str = os.getenv("PRIVATE_KEY", "")
NODE = os.getenv("NODE", "")

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)-8s] - %(message)s (%(filename)s:%(lineno)s)",
    "%Y-%m-%d %H:%M:%S",
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)-8s] - %(message)s (%(filename)s:%(lineno)s)",
    level=logging.INFO,
    handlers=[handler],
)

log = logging.getLogger(__name__)

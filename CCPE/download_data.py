import gdown
import os, sys
from zipfile import ZipFile
import logging

logger = logging.getLogger(__name__)

# go to parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from utils import *

gdrive_template = "https://drive.google.com/uc?id="
file_name = "CCPE.zip"
file_dir = "CCPE/data"

if __name__ == "__main__":
    file_id = "1pqR3ENb9bYtW2v5DpewWjbMEQ0fdznDl"
    url = gdrive_template + file_id

    os.makedirs(file_dir, exist_ok=True)
    file_path = os.path.join(file_dir, file_name)

    logger.info("Downloading CCPE file!")

    gdown.download(url, file_path, quiet=False)

    with ZipFile(file_path, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall(file_dir)
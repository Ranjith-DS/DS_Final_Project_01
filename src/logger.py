import logging
import os
from datetime import datetime

# Defining the log file name using current date and time format.
FILE_NAME = f"{datetime.now().strftime('%M-%d-%Y-%H-%M-%S')}.logs"

# Defining the directory path where the log file will be saved.
LOG_FOLDER_PATH = os.path.join(os.getcwd(),"logs")

#Creates the directory in the name of  logs even if already exist.
os.makedirs(LOG_FOLDER_PATH,exist_ok=True)

# Defining the complete path for the folder and the file
LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH,FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #Log message formate
    level=logging.INFO
)
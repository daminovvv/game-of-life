import os
from dotenv import load_dotenv

load_dotenv()
DIRECTORY = os.getenv("DIRECTORY")
FILENAME = os.getenv("FILENAME")
PATH = f'{DIRECTORY}/{FILENAME}'

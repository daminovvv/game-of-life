import json
import os

from src.models import BoardClass
from config import DIRECTORY, PATH


def clean_json():
    path = DIRECTORY
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    with open(PATH, "w") as file:
        pass


def write_to_json(current_board: BoardClass, data: dict) -> None:
    """ Writes current board and data to json"""

    data[str(current_board.move)] = current_board.__dict__

    if len(data) > 5:
        oldest_key = min(list(map(int, data.keys())))
        del data[str(oldest_key)]

    with open(PATH, "w") as file:
        json.dump(data, file)


def read_last_from_json() -> (BoardClass, dict):
    """ Returns last board object and json data"""
    try:
        with open(PATH, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    latest_key = max(list(map(int, data.keys())))

    return BoardClass(**data[str(latest_key)]), data

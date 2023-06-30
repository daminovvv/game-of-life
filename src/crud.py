import json

from src.models import BoardClass


def clean_json():
    filename = "data.json"
    with open(filename, "w") as file:
        pass


def write_to_json(current_board: BoardClass, data: dict) -> None:
    """ Writes current board and data to json"""
    filename = "data.json"

    data[str(current_board.move)] = current_board.__dict__

    if len(data) > 5:
        oldest_key = min(list(map(int, data.keys())))
        del data[str(oldest_key)]

    with open(filename, "w") as file:
        json.dump(data, file)


def read_last_from_json() -> (BoardClass, dict):
    """ Returns last board object and json data"""
    filename = "data.json"
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    latest_key = max(list(map(int, data.keys())))

    return BoardClass(**data[str(latest_key)]), data


def game_over(current_board, data) -> bool:
    """ Checks if current state of the board matches last 5 states"""
    for key in data:
        if current_board.board == data[key]["board"]:
            return True
    return False

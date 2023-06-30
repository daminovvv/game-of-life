from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.crud import write_to_json, read_last_from_json, game_over, clean_json
from src.models import BoardClass

router = APIRouter(
    prefix="/game-of-life",
    tags=["GameOfLife"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/rules", response_class=HTMLResponse)
def welcome_page(request: Request):
    return templates.TemplateResponse("rules_page.html", {"request": request})


@router.get("/new_game", response_class=HTMLResponse)
def start(request: Request):
    clean_json()
    data = {}
    current_board = BoardClass()
    write_to_json(current_board, data)
    return templates.TemplateResponse("game_page.html", {"request": request, "current_board": current_board})


@router.get("/move", response_class=HTMLResponse)
def next_move(request: Request):
    try:
        current_board, data = read_last_from_json()
    except ValueError:
        return templates.TemplateResponse("error_page.html", {
            "request": request,
            "message": "Not Found 404. No current game available. Start new game."
        })
    current_board.update_board()

    if game_over(current_board, data):
        return templates.TemplateResponse("game_page.html", {
            "request": request,
            "current_board": current_board,
            "game_over": True
        })

    write_to_json(current_board, data)
    return templates.TemplateResponse("game_page.html", {"request": request, "current_board": current_board})

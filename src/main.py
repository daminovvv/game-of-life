import uvicorn
from fastapi import FastAPI

from src.pages.router import router as game_of_life_router

app = FastAPI(
    title="Conway's Game of Life"
)

app.include_router(game_of_life_router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)

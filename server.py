from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pyspiel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

game = pyspiel.load_game("tic_tac_toe")
state = game.new_initial_state()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/game_state")
async def get_game_state():
    return JSONResponse(content=state.observation_tensor())

@app.post("/apply_action")
async def apply_action(action: int):
    if action in state.legal_actions():
        state.apply_action(action)
    return JSONResponse(content=state.observation_tensor())

# Run the server with `uvicorn filename:app --reload`

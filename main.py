import uuid
import random

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 

app = FastAPI()

games = {}

@app.post("/games")
def create_game():
    game_id = str(uuid.uuid4())
    secret = random.randint(1,100)
    games[game_id] = secret
    return {"game_id": game_id}

class GuessRequest(BaseModel):
    guess: int

@app.post("/games/{game_id}/guesses")
def make_guess(game_id: str, guess:int):
    # Check if the game ticket actually exists
    if game_id not in games:
        raise HTTPException(status_code=404, detail= "Game not found")
    if guess < 1 or guess > 100:
        raise HTTPException(status_code=400, detail= "Guess is out of bounds")
    secret = games[game_id]
    result = check_guess(secret, guess)
    return {"result":result}


def check_guess(secret: int, guess: int) -> str:
    if guess == secret: 
        return "correct"
    elif guess > secret: 
        return "too high, go lower"
    else: 
        return "too low go higher"
    
@app.get("/")
def read_index():
    return FileResponse("index.html")
# Number Guessing Game

A small number-guessing game built to learn the request and response cycle. A FastAPI back end keeps the secret number and decides each result, and a plain HTML/JavaScript page lets you play.

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/ and click "Start New Game".
API docs are generated automatically at http://127.0.0.1:8000/docs.

## Test it

```bash
pytest
```

## Endpoints

- `GET /` serves the game page.
- `POST /games` starts a game and returns a `game_id`. The secret number stays on the server.
- `POST /games/{game_id}/guesses?guess=N` returns `{"result": ...}` ("correct", "too high", or "too low").
  - `404` if the game doesn't exist
  - `400` if the guess is outside 1 to 100
  - `422` if the guess isn't an integer

## Notes

Games are stored in memory, so they reset when the server restarts. A database would be the next step.

from fastapi.testclient import TestClient
from main import app
from main import check_guess

client = TestClient(app)

def test_guess_out_of_range_returns_400():
    created = client.post("/games")
    game_id = created.json()["game_id"]
    response = client.post(f"/games/{game_id}/guesses?guess=500")
    assert response.status_code == 400

def test_unknown_game_returns_404():
    response = client.post("/games/not-a-real-id/guesses?guess=50")
    assert response.status_code == 404

def test_correct_guess():
    assert check_guess(57, 57) == "correct"

def test_too_high():
    assert check_guess(50, 80) == "too high, go lower"

def test_too_low():
    assert check_guess(50, 20) == "too low go higher"
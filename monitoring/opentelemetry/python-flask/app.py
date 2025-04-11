from random import randint
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@app.route("/rolldice", methods=["GET"])
def roll_dice() -> str:
    """
    Endpoint to roll a dice. Logs the result and returns it.
    If a player name is provided, it logs the player's name along with the result.
    """
    player = request.args.get("player", default=None, type=str)
    result = roll()

    if player:
        logger.info(f"Player '{player}' rolled the dice: {result}")
    else:
        logger.info(f"Anonymous player rolled the dice: {result}")

    return jsonify({"player": player or "Anonymous", "result": result})


def roll() -> int:
    """
    Simulates rolling a six-sided dice and returns the result.
    """
    return randint(1, 6)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
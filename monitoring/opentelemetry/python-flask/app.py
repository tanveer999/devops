from random import randint
from flask import Flask, request, jsonify
import logging

from opentelemetry import trace

# Acquire a tracer
tracer = trace.get_tracer("diceroller.tracer")

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

    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
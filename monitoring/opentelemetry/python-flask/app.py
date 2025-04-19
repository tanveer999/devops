from random import randint
from flask import Flask, request, jsonify
import logging
from pymongo import MongoClient

from opentelemetry import trace

# Acquire a tracer
tracer = trace.get_tracer("diceroller.tracer")

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Configure mongo client
mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["dice_db"]
collection = db["dice_rolls"]

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


@app.route("/latest-records", methods=["GET"])
def get_latest_records() -> str:
    """
    Endpoint to fetch latest 10 records from the database.
    """

    with tracer.start_as_current_span("get_latest_records") as span:
        try:
            records = list(collection.find().sort("_id", -1).limit(10))
            span.set_attribute("db.collection", "dice_rolls")
            span.set_attribute("db.operation", "find")
            span.set_attribute("records.count", len(records))

            return jsonify({"records": records})
        
        except Exception as e:
            span.record_exception(e)
            logger.error(f"Error fetching records: {e}")
            return jsonify({"error": "Failed to fetch records"}), 500 

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
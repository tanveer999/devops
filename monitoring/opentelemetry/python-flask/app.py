from random import randint
from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/rolldice")
def roll_dice():
  player = request.args.get('player', default=None, type=str)
  result = str(roll())
  if player:
    logger.warning(f'{player} is rollin the dice: {result}')
  else:
    logger.warning(f'Anonymous player is rolling the dice: {result}')
  
  return result


def roll():
  return randint(1, 6)
from flask import Flask, request
from wtforms import StringField, validators, PasswordField, Form
import random


app = Flask(__name__)


@app.route("/", methods=['GET'])
def start_game():
    if request.method == 'GET':
        return "NUMBER is made up"


def new_number():
    return random.randint(1, 10)


def game_over():
    return "game over"


SECRET_NUMBER = new_number()


@app.route("/guess", methods=['POST'])
def start():
    if request.method == 'POST':
        data = request.values
        my_num = data['number']
        while my_num != SECRET_NUMBER:
            print(my_num)
            print(SECRET_NUMBER)
            if int(my_num) < SECRET_NUMBER:
                return '>'
            elif int(my_num) > SECRET_NUMBER:
                return '<'
            else:
                return '=', game_over()


if __name__ == "__main__":
    app.debug = True
    app.run()

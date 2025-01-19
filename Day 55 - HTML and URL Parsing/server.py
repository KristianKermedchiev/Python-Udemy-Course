from flask import Flask
import random

app = Flask(__name__)

choice = random.randint(1, 10)


@app.route('/')
def hello():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExODl3dWc3NWFpYmsyZzNxZXQxbm9lNTR0bmg2dmFmYWxtN'
            'DdpMWo3eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S65GkxL15Z8uGTF8Zl/giphy.gif>')


@app.route('/<int:number>')
def guess(number):
    if number == choice:
        return '<h1>Correct!</h1>'
    elif number > choice:
        return '<h1>Too high!</h1>'
    elif number < choice:
        return '<h1>Too low!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
import random
import datetime
import requests

url_agify = "https://api.agify.io?name="
url_genderize = "https://api.genderize.io?name="

app = Flask(__name__)


@app.route('/')
def index():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("home.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    response_agify = requests.get(url_agify + name)
    response_genderize = requests.get(url_genderize + name)

    return render_template("index.html",
                           name=name,
                           age=response_agify.json()['age'],
                           gender=response_genderize.json()['gender'])


if __name__ == '__main__':
    app.run(debug=True)

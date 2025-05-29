from flask import Flask, render_template
import datetime
from markupsafe import escape
app = Flask(__name__)
import requests

agify_url = "https://api.agify.io/"
gender_url = "https://api.genderize.io"


@app.route('/')
def home():
    year = datetime.date.today().year
    return render_template("index.html", the_year=year)

@app.route('/guess/<entered_name>')
def name_guess(entered_name):

    parameters = {'name': entered_name}
    age = requests.get(agify_url, parameters).json()["age"]
    gender = requests.get(gender_url, parameters).json()["gender"]
    print(gender)
    #return f"your name is {escape(entered_name)}"
    return render_template("guess.html", guessed_age=age, uname=entered_name, guessed_gender=gender)




if __name__ == "__main__":
    app.run(debug=True)
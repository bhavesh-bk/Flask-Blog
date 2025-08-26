from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)

@app.route('/username/<name>')
def guess(name):
    gender_api = requests.get(f"https://api.genderize.io?name={name}")
    genders = gender_api.json()
    gender = genders['gender']

    age_api = requests.get(f"https://api.agify.io?name={name}")
    ages = age_api.json()
    age = ages['age']
    return render_template("guess.html", person_name = name,gender=gender,  age=age)

@app.route('/blog')
def get_blog():
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    blog_api = requests.get(blog_url)
    blog_data = blog_api.json()
    return render_template("blog.html",posts = blog_data)

if __name__ == "__main__":
    app.run(debug=True)
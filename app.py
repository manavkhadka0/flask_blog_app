from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

posts = [

    {
        'author':"Manav Khadka",
        'title':'Data Science',
        'content':"First POst of Manav",
        'date_posted':'April 20,2021'
    },
    {
        'author':"Manav Khadka",
        'title':'Machine Learning',
        'content':"First POst ",
        'date_posted':'April 29,2021'
    },

]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)

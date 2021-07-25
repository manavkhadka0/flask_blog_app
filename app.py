from flask import Flask
from flask.templating import render_template
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app['SECRET_KEY'] = '3c95d6d458a4270ed104b2f1c98dd39a'


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
    return render_template('about.html',title="About")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title="Register",form=form)

@app.route('/login')
def login():
    return render_template('login.html',title="Login")


if __name__ == "__main__":
    app.run(debug=True)

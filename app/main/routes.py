from flask import render_template,Blueprint


main = Blueprint('main',__name__)



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

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html',posts=posts)


@main.route('/about')
def about():
    return render_template('about.html',title="About")

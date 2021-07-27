
from app.users.utils import send_confirmation_email
from app.models import User
from flask import render_template,redirect,Blueprint,flash,url_for,request
from app.users.forms import RegistrationForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required
from app import bcrypt,db

users = Blueprint('users',__name__)

@users.route('/register',methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('url_for(main.home)')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        send_confirmation_email(user)
        flash('An email has been sent with instructions to verify your account.', 'info')
        return redirect(url_for('users.login'))
    return render_template('register.html',title="Register",form=form)


@users.route("/register/<token>", methods=['GET', 'POST'])
def verification_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_confirmation_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.login'))
    user.confirm = True
    db.session.commit()
    flash(f'Account created! You can now login', 'success')
    return redirect(url_for('users.login'))



@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.confirm == False:
            flash('Login Unsuccessful. Verify your account', 'danger')
        if user and bcrypt.check_password_hash(user.password,form.password.data) and user.confirm == True:
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check Email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
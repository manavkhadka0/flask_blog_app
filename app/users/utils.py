from flask_mail import Message
from app import mail
from flask import url_for

def send_confirmation_email(user):
    token = user.get_confirmation_token()
    msg = Message('Account Verification',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To verify your account, visit the following link:
{url_for('users.verification_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
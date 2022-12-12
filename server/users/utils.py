import smtplib
from email.message import EmailMessage


def send_passwordreset_email(user_mail, token, userid):
    msg = EmailMessage()
    msg['Subject'] = 'Password rest'
    msg['From'] = 'abhishek.9867.338961@gmail.com'
    msg['To'] = user_mail

    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">Password Reset</h1>
            <p>Click <a href="http://localhost:8000/api/auth/reset/{token}/{userid}">here</a> to reset the password</p>
        </body>
    </html>
    """, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('abhishek.9867.338961@gmail.com', 'wmjlbyviwunhgzkr')
        smtp.send_message(msg)

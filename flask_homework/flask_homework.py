from flask import Flask, request
from wtforms import StringField, validators, PasswordField, Form


application = Flask(__name__)
# application.config.update(
#     DEBUG=True,
#     SECRET_KEY='This key must be secret!',
#     WTF_CSRF_ENABLED=False,
# )


class check_user(Form):
    email = StringField(label='email', validators=[
        validators.email(),
    ])
    password = PasswordField(label='password', validators=[
        validators.EqualTo('confirm', message='passwords must match'),
        validators.length(min=6)
    ])
    confirm = PasswordField(label='confirm')


@application.route("/check_file/<path:value>")
def look_for_file(value):
    try:
        with open(value, mode='r') as f:
            if f:
                return f.read()
    except Exception as e:
        return "404 File not found"


@application.route('/form/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        print(request.form)
        form = check_user(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200



if __name__ == '__main__':
    application.debug = True
    application.evn = "Working hard"
    application.run()

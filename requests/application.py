from flask import Flask

application = Flask(__name__)


@application.route("/")
def index_html():
    return "<b><font color = blue> hello from flask main page</font></b>"


@application.route("/help2")
@application.route("/help")
def help_page():
    return "nothing to help you with"


@application.route("/users")
def users_main_page():
    return "Users main page"


@application.route("/users/<username>")
def show_user_page(username):
    return username.upper() + " page"


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "SubPath is: " + subpath


@application.route("/pow/<int:x>")
def cal_pow(x):
    return "Pow of " + str(x) + " is " + str(x**2)


@application.route("/htmlpage")
def show_html():
    with open("myhtml.html", mode='r') as page:
        return page.read()



if __name__ == "__main__":
    application.debug = True
    application.evn = "Working hard"
    application.run()

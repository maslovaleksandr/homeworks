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


@application.route("/long/<value1>/<value2>/<value3>")
def find_longest(value1, value2, value3):
    max_value = max(len(value1), len(value2), len(value3))
    return str(max_value)


@application.route("/sum/<int:x>/<int:y>")
def cal_pow(x, y):
    return "Sum x,y is: " + str(x+y)


@application.route("/check_file/<path:value>")
def look_for_file(value):
    with open(value, mode='r') as f:
        if f:
            return "File exists"
        else:
            return "File no exists"



@application.route("/htmlpage")
def show_html():
    with open("myhtml.html", mode='r') as page:
        return page.read()



if __name__ == "__main__":
    application.debug = True
    application.evn = "Working hard"
    application.run()

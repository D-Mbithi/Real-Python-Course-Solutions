from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def index():
    """Index routing."""
    return "Hello world"


@app.route('/test/<search_query>')
def search(search_query):
    """Search routing."""
    return search_query


@app.route('/integer/<int:value>')
def int_type(value):
    """Integer value routing."""
    print(value + 1)
    return "correct"


@app.route("/path/<path:value>")
def path_type(value):
    """Path value routing."""
    print(value)
    return "correct"


@app.route("/name/<name>")
def home(name):
    """Home routing view."""
    if name.lower() == 'dennis':
        return "Hello, {}".format(name), 200
    else:
        return "Not found", 404


if __name__ == "__main__":
    app.run(debug=True)

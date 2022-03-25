from flask import Flask
from flask_cors import CORS
from data import make_graph
from api import max_free_slots

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://www.sociogame.net"]}})


@app.route("/user/<screen_name>")
def network_graph(screen_name):
    return make_graph(screen_name)


@app.route("/slots")
def limit():
    return str(max_free_slots())


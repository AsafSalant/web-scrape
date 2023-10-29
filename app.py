from flask import Flask
import newspaper
from newspaper import Article
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

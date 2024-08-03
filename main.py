from flask import Flask

app = Flask(__name__)
from urls import *
app.secret_key = "shubhada"
if (__name__ == "__main__"):
    app.run(debug=True)
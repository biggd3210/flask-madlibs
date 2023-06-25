from flask import Flask, request
from stories import Story

app = Flask(__name__)

@app.route(/)
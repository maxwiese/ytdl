from flask import render_template, request

from server import app
from engine import FindAndDownload

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    FindAndDownload("sweetbutpsyco")
    return "ok"
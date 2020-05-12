from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    task = request.form.get('task')
    return render_template('index.html', task=task)
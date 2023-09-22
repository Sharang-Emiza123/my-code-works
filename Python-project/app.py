from flask import Flask, render_template, url_for, redirect, request
import requests
import pandas as pd
from expManager import checkking

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST', 'GET'])
def HomePage():
    usrnm = request.args.get('Username')
    return render_template('homepage.html')

@app.route('/exmgr', methods=['POST', 'GET'])
def expMgr():
    return checkking()

if __name__ == '__main__':
	app.run(debug=True)
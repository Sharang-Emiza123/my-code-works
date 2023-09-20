from flask import Flask, render_template, url_for, redirect, request
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def HomePage():
    usrnm = request.args.get('Username')
    return render_template('homepage.html')


if __name__ == '__main__':
	app.run(debug=True)
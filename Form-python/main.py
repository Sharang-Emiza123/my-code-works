from flask import Flask, render_template, url_for, redirect, request
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/')
def load():
    return render_template('form-py.html')

@app.route('/a')
def getData():
      fname = request.args.get('fname')
      lname = request.args.get('lname')
      age = request.args.get('age')
      city = request.args.get('city')
      arr1 = [fname, lname, age, city]
      



akjdfhaiudhfkajbdgit branch -d old-branch.









if __name__ == '__main__':
	app.run(debug=True)

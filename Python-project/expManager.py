from flask import Flask, render_template, url_for, redirect, request
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/exmgr', methods=['POST', 'GET'])
def checkking():
    return render_template('ExpenseManager/index.html')

@app.route('/exmgr/add', methods=['POST', 'GET'])
def addExp():
    return render_template('ExpenseManager/addExpense.html')    
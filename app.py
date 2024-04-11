import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort
from datetime import datetime
import graph
import stock_query

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'

# Function to open a connection to the database.db file
@app.route('/chart', methods=['GET'])
def chart_form():
    return render_template('chart.html')

@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    symbol = request.form['stock_symbol']
    start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d")
    chart_type = int(request.form['chart_type'])
    time_series = int(request.form['time_series'])
    data = stock_query.get_stock_data(time_series, symbol)

    chart = graph.generate_graph(data, chart_type, time_series, start_date, end_date, symbol)

    return render_template('chart.html', chart=chart.render())

app.run(host="0.0.0.0")
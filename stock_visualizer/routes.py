from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import StockForm
from .charts import *

@app.route("/", methods = ['GET', 'POST'])
@app.route("/stocks", methods = ['GET', 'POST'])
def stocks():

    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Get the form data to query the api
            symbol = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])

            if end_date <= start_date:
                # Generate an error message
                err = "ERROR! End date cannot be earlier than the start date!"
                chart = None
            else:
                # Query the api here using the form data
                err = None

                # THIS IS WHERE YOU CALL THE METHODS FROM (CHARTS.PY) AND IMPLEMENT YOUR CODE

                # This chart variable is what is passed to the (stock.html) page to render the returned chart
                chart = "ASSIGN CHART TO THIS VARIABLE HERE"

            return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
        
    return render_template("stock.html", form = form, template = "form-template")
"""
THIS WEB SERVICE EXTENDS THE ALPHAVANTAGE API BY CREATING A VISUALIZATION MODULE,
CONVERTING JSON QUERY RESULTS RETURNED FROM THE API INTO CHARTS AND OTHER GRAPHICS.

THIS IS WHERE YOU SHOULD ADD THE CODE TO QUERY THE API
"""

import requests
from datetime import datetime
from datetime import date
import pygal

# Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()
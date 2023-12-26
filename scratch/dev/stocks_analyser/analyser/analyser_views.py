from django.shortcuts import render,redirect
import pandas as pd
from .analyser_models import Equity_Paramters
from django.db import connections
import datetime as dt
from db_functions import db_methods

dbm=db_methods()

def update_analyser_equity_parameter(request):
    
    return render(request,'analyser/customer/customer.html')
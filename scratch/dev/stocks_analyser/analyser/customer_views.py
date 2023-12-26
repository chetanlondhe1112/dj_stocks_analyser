from django.shortcuts import render,redirect
from sqlalchemy import create_engine
import pandas as pd
from .models import Equity_Files
from django.db import connections
import datetime as dt


def customer(request):
    return render(request,'analyser/customer/customer.html')

def add_customer(request):
    return render(request,'analyser/customer/add_customer.html')
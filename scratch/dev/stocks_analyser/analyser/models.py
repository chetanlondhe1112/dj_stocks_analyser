from django.db import models

# Create your models here.

class File(models.Model):
    file=models.FileField(upload_to="files")

class Equity_Files(models.Model):
    username=models.CharField(max_length=20)
    datetime=models.DateTimeField()
    equity_file_name=models.CharField(max_length=200,unique=False)
    name=models.CharField(max_length=50)	
    bse_code=models.CharField(max_length=50)
    nse_code=models.CharField(max_length=50)
    industry=models.CharField(max_length=200)
    current_price=models.FloatField(default=0.0)
    market_capitalization=models.FloatField(default=0.0)
    price_to_earning=models.FloatField(default=0.0)
    industry_pe=models.FloatField(default=0.0)
    eps=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.equity_file_name


class Equity_Filter(models.Model):
    username=models.CharField(max_length=20)
    datetime=models.DateTimeField()
    equity_filter_name=models.CharField(max_length=200)
    parameter_name=models.CharField(max_length=100)	
    condition_1=models.CharField(max_length=10)
    value_1=models.CharField(max_length=10000)
    result_1=models.CharField(max_length=10)
    condition_2=models.CharField(max_length=10)
    value_2=models.CharField(max_length=10000)
    result_2=models.CharField(max_length=10)
    def __str__(self):
        return self.equity_filter_name
    
class Customer_Register(models.Model):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    pwd=models.CharField(max_length=100)

    pan=models.IntegerField()
    aadhar=models.IntegerField()
    mobileno=models.IntegerField()
    
    angel_user=models.CharField(max_length=100)
    angel_pwd=models.CharField(max_length=100)
    fin_q=models.IntegerField()
    totpkey=models.CharField(max_length=500)
    initialdeposit=models.FloatField()
    available_margin=models.FloatField()
    lotsize=models.IntegerField()
    apikey=models.CharField(max_length=500)
    asmita_apikey=models.CharField(max_length=500)
    ha_apikey=models.CharField(max_length=500)
    status=models.IntegerField()
    strategyflag=models.IntegerField()

    signupdate=models.DateTimeField()
    createdate=models.DateTimeField()
    user_table_id=models.IntegerField()
    def __str__(self):
        return self.first_name
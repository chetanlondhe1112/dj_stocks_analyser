from django.db import models

# Create your models here.

class Equity_Paramters(models.Model):
    create_datetime=models.DateTimeField()
    equity_file_name=models.CharField(max_length=200,unique=False)
    equity_parameter_name=models.CharField(max_length=50)	
    def __str__(self):
        return self.equity_parameter_name
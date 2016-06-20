from django.db import models

class SerialNumbers(models.Model):
    serialnumber_text = models.CharField(max_length=200)
    
# Create your models here.

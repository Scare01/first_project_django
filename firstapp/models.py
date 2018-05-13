from django.db import models

class Dreamreal(models.Model):
    wensite = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = "dreamreal"


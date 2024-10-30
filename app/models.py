from django.db import models

# Create your models here.
class Bus_table(models.Model):
    bus_name = models.CharField(max_length=100,primary_key=True)
    bus_num = models.IntegerField()
    def __str__(self):
        return self.bus_name
class Passengers(models.Model):
    bus_name = models.ForeignKey(Bus_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobial = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name



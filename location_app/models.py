from django.db import models
from datetime import datetime

# Create your models here.



class Country(models.Model):

    country_name = models.CharField(max_length=100, blank=True, null=True)
    country_status = models.BooleanField(default=True)
    country_created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country_ref = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100, null=True, blank=True)
    state_status = models.BooleanField(default=True)
    state_created_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.state_name

class City(models.Model):
    country_ref = models.ForeignKey(Country,on_delete=models.CASCADE)
    state_ref = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100, null=True, blank=True)
    city_status = models.BooleanField(default=True)
    city_created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.city_name


class Area(models.Model):
    country_ref = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_ref = models.ForeignKey(State, on_delete=models.CASCADE)
    city_ref = models.ForeignKey(City,on_delete=models.CASCADE)
    area_name = models.CharField(max_length=100, null=True, blank=True)
    area_status = models.BooleanField(default=True)
    area_created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.area_name


class Person(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    person_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    country_ref = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_ref = models.ForeignKey(State, on_delete=models.CASCADE)
    city_ref = models.ForeignKey(City, on_delete=models.CASCADE)
    area_ref = models.ForeignKey(Area, on_delete=models.CASCADE)
    person_status = models.BooleanField(default=True)
    person_created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.person_name

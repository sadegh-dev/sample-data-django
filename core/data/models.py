from django.db import models
from datetime import datetime


class DataEn(models.Model):
    
    # Number
    the_integer =   models.IntegerField(blank=True, null=True)
    the_pos_integer = models.PositiveIntegerField(blank=True, null=True)
    the_float = models.FloatField(blank=True, null=True)
    
    # Json
    the_json = models.JSONField(blank=True, null=True)
    
    # Boolean
    the_boolean = models.BooleanField(blank=True, null=True)
    
    # String
    the_char = models.CharField(max_length=200,blank=True, null=True)
    the_text = models.TextField(max_length=1000, blank=True, null=True)
    
    # Date / Time
    the_time = models.TimeField(blank=True, null=True)
    the_date = models.DateField(blank=True, null=True)
    the_date_time = models.DateTimeField(default = datetime.now)
    
    # Email
    the_email = models.EmailField(max_length=254, blank=True, null=True)

    # Slug
    the_slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)

    # Url
    the_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.the_slug




class DataFa(models.Model):
    pass
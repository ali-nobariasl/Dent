from django.db import models

class first(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Id = models.IntegerField(primary_key=True, auto_created=True) 
from django.db import models

# Create your models here.
class SearchedLinks(models.Model):
	keyword= models.CharField(max_length=500,null =True, blank = True)
	link = models.CharField(max_length=500,null =True, blank = True)
    
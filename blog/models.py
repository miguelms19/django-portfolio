from django.db import models
import datetime
# Create your models here.

class BlogConfig(models.Model):

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#Add Blog app to the settings

# Create a migration

# Migrate

# add to the admin

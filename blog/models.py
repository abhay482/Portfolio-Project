from django.db import models

# Create your models here.

class blog(models.Model):
    tital = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField()


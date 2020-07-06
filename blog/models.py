from django.db import models

# Create your models here.

class blog(models.Model):
    tital = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.tital


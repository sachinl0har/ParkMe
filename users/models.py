from django.db import models

# Create your models here.

class userContact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
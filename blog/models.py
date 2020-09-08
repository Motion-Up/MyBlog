from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=300)
    date = models.DateTimeField(null=True)
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')


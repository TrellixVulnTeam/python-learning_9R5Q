from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "media/")

    def __str__(self):
        return self.title

    def custom_date(self):
        return self.pub_date.strftime("%b %d %Y")

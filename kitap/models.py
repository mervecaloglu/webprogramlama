from django.db import models

class Kitap(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_time = models.DateTimeField()

    def __str__(self):
        return self.title

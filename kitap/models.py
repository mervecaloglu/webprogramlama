from django.db import models

class Kitap(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Yorum(models.Model):
    kitap = models.ForeignKey(Kitap, on_delete=models.CASCADE, related_name='yorumlar')
    isim = models.CharField(max_length=100)
    yorum = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.isim} - {self.kitap.title}"

from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class News(models.Model):
    head = models.CharField(max_length=64)
    text = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.head



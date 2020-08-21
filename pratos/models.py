from django.db import models

# Create your models here.
class Choice(models.Model):
    name = models.CharField(max_length=50)
    preço = models.FloatField()

    def __str__(self):
        return self.name

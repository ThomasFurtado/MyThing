from django.db import models

# Create your models here.
class Choice(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

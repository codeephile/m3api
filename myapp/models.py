from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.name
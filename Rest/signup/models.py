from django.db import models

# Create your models here.
class SignUp(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.name
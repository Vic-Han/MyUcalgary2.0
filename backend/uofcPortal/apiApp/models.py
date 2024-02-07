from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.email


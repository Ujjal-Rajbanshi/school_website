from django.db import models

# Create your models here.
class FormModel(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name
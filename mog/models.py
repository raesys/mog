from django.db import models


class Mog(models.Model):
    title = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15,)
    name_of_church = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='static/img/mog')

    def __str__(self):
        return self.full_name

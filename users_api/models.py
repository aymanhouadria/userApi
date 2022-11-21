from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=False,)
    email = models.EmailField(null=False)
    birthdate = models.DateField(null=False)
    address = models.ForeignKey('Address', on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.name)


class Address(models.Model):
    street = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)
    zip = models.CharField(max_length=10, blank=False)

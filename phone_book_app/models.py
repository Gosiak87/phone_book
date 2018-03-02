from django.db import models

# Create your models here.


class Address(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    number_house = models.IntegerField(null=True)
    number_flat = models.IntegerField(null=True)


class Phone(models.Model):
    TYPE_PHONE = (
        (0, "domowy"),
        (1, "służbowy"),
        (2, "komórkowy"),
    )

    type_phone = models.IntegerField(choices=TYPE_PHONE, default=2)
    number_phone = models.IntegerField(null=True)

class Email(models.Model):
    TYPE_EMAIL = (
        (0, "prywatny"),
        (1, "służbowy"),
    )

    type_email = models.IntegerField(choices=TYPE_EMAIL, default=1)
    address_email = models.CharField(max_length=25, null=True)


class Groups(models.Model):
    name = models.CharField(max_length=128)


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    person_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    person_email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True)
    person_phone = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True)
    group = models.ManyToManyField(Groups)
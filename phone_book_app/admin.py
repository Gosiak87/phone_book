from django.contrib import admin
from .models import Address, Phone, Email, Person

my_classes = [Address, Phone, Email, Person]

for class_ in my_classes:
    admin.site.register(class_)





from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from phone_book_app.models import Address, Person, Phone, Email

# Create your views here.


class AddPerson(View):
    def get(self, request):
        return render(request, "add_person.html", {})

    def post(self, request):
        req_1 = request.POST.get("first_name")
        req_2 = request.POST.get("last_name")
        req_3 = request.POST.get("description")
        Person.objects.create(first_name=req_1, last_name=req_2, description=req_3)
        new_person = Person.objects.get(first_name=req_1, last_name=req_2, description=req_3)
        return render(request, "new_person.html", {"new_person": new_person})


class ModifyPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        # address_id = person.person_address_id
        # address = Address.objects.get(id=address_id)
        #
        # email_id = person.person_email_id
        # address_email = Email.objects.get(id=email_id)

        # phone_id = person.person_phone_id
        # number_phone = Phone.objects.get(id=phone_id)
        # wyciagnelam konkretny obiekt po id = id
        return render(request, "modify_person.html", {"person": person}) # "address": address, "address_email": address_email , "number_phone": number_phone})

    def post(self, request, id):
        person = Person.objects.get(id=id)

        # Wyciąganie ID
        address_id = person.person_address_id
        address = Address.objects.get(id=address_id)

        email_id = person.person_email_id
        address_email = Email.objects.get(id=email_id)

        phone_id = person.person_phone_id
        number_phone = Phone.objects.get(id=phone_id)

        # Odpowiedz Posta /inputy

        req_1 = request.POST.get("first_name")
        req_2 = request.POST.get("last_name")
        req_3 = request.POST.get("description")
        req_4 = request.POST.get("city")
        req_5 = request.POST.get("street")
        req_6 = request.POST.get("number_house")
        req_7 = request.POST.get("number_flat")
        req_8 = request.POST.get("address_email")
        req_9 = request.POST.get("number_phone")

        if req_1 in request.POST["first_name"]:
            person.first_name = req_1
            person.save()
        if req_2 in request.POST["last_name"]:
            person.last_name = req_2
            person.save()
        if req_3 in request.POST["description"]:
            person.description = req_3
            person.save()
        if req_4 in request.POST["city"]:
            address.city = req_4
            address.save()
        if req_5 in request.POST["street"]:
            address.street = req_5
            address.save()
        if req_6 in request.POST["number_house"]:
            address.number_house = req_6
            address.save()
        if req_7 in request.POST["number_flat"]:
            address.number_flat = req_7
            address.save()
        if req_8 in request.POST["address_email"]:
            address_email.address_email = req_8
            address_email.save()
        if req_9 in request.POST["number_phone"]:
            number_phone.number_phone = req_9
            number_phone.save()

        return HttpResponse("Zedytowano osobę")


class AddAddress(View):

    def get(self, request, id):
        person = Person.objects.get(id=id)   # wyciagnelam konkretny obiekt po id = id
        return render(request, "add_address.html", {"person": person})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        req_1 = request.POST.get("city")
        req_2 = request.POST.get("street")
        req_3 = int(request.POST.get("number_house"))
        req_4 = int(request.POST.get("number_flat"))
        Address.objects.create(city=req_1, street=req_2, number_house=req_3, number_flat=req_4)
        person_address_id = Address.objects.get(city=req_1, street=req_2, number_house=req_3, number_flat=req_4)
        person.person_address_id = person_address_id
        return HttpResponse("Dodano Adres")


class DeletePerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)  # wyciagnelam konkretny obiekt po id = id
        person.delete()
        return HttpResponse("Osoba została usunięta")


class ShowPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        adres_id = person.person_address_id
        adres = Address.objects.get(id=adres_id)
        email_id = person.person_email_id
        email = Email.objects.get(id=email_id)
        phone_id = person.person_phone_id
        phone = Phone.objects.get(id=phone_id)
        return render(request, "show_person.html", {"person": person,"adres": adres, "email": email, "phone": phone})


class AllPerson(View):
    def get(self, request):
        persons = Person.objects.all().order_by("first_name")
        return render(request, "all_person.html", {"persons": persons})


class AddPhone(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)   # wyciagnelam konkretny obiekt po id = id
        return render(request, "add_phone.html", {"person": person})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        #req_1 = request.POST.get("type_phone")
        req_2 = request.POST.get("number_phone")
        Phone.objects.create(number_phone=req_2)
        person_phone_id = Phone.objects.get(number_phone=req_2)
        person.person_phone_id = person_phone_id
        person.save()
        return HttpResponse("Dodano telefon")


class AddEmail(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)   # wyciagnelam konkretny obiekt po id = id
        return render(request, "add_email.html", {"person": person})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        #req_1 = request.POST.get("type_email")
        req_2 = request.POST.get("address_email")
        Email.objects.create(address_email=req_2)
        person_email_id = Email.objects.get(address_email=req_2)
        person.person_email_id = person_email_id      # połączenie relacją
        person.save()
        return HttpResponse("Dodano email")







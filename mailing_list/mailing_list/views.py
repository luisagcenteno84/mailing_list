from django.shortcuts import render
from .models import Contact

def mailing_list(request, name):
    c_list = Contact.objects.filter(name__startswith=name)
    context = {name: name, 'c_list': c_list}
    return render(request, 'contact.html', context)
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm






class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("thanks")


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")
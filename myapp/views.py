# from django.http import HttpResponse
from django.shortcuts import render

from . import models
from django.core import serializers
from datetime import datetime
import json
from . import forms

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = forms.BookingForm()
    if request.method == 'POST':
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add code for the bookings() view
def bookings(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = models.Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)

    return render(request, 'bookings.html', {"bookings" : booking_json})

def menu(request):
    menu_data = models.Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = models.Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 
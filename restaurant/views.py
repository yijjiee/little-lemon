from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializer import MenuSerializer, BookingSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    pass

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

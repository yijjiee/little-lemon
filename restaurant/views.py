from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializer import MenuSerializer, BookingSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    authentication_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    pass

class BookingViewSet(viewsets.ModelViewSet):
    authentication_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

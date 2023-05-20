from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import UserSerializer, TicketSerializer, CategorySerializer
from .models import Ticket, Category

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
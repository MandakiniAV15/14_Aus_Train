from django.shortcuts import render
from .models import student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class StudentModelViewSet(viewsets.modelViewSet):
    queryset = student.objects.all()
    serializers_class = StudentSerializer
    authentication_classes = [BaseAuthentication]
    permissions_class = [IsAuthenticated]

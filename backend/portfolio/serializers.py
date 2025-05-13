from rest_framework import serializers
from .models import Project, Contact
from django.core.mail import send_mail
from django.conf import settings

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Project, Contact
from .serializers import ProjectSerializer, ContactSerializer
from django.core.mail import send_mail
from django.conf import settings

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Send email to you
        subject = f"New Contact Message from {instance.name}"
        message = f"Name: {instance.name}\nEmail: {instance.email}\n\nMessage:\n{instance.message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['mohammadsrd25@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
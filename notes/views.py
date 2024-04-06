from django.shortcuts import render
from .models import Note
from rest_framework import viewsets
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by("-created")
    serializer_class = NoteSerializer



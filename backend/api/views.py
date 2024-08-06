from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Note

#ListCreate both lists all notes the user has created, and allows the user to create a new note
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() ### ensure we don't create a duplicate
    serializer_class = UserSerializer ### data required to make a new user (username, password)
    permission_classes = [AllowAny] ### anyone can create call this view, even if they aren't a user yet

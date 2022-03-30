from rest_framework import viewsets
from .models import Questionnaire, Question, Reponse, ReponseUser, Note
from .serializers import QuestionnaireSerializer, QuestionSerializer, ReponseSerializer, NoteSerializer, ReponseUserSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ReponseViewSet(viewsets.ModelViewSet):
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ReponseUserViewSet(viewsets.ModelViewSet):
    queryset = ReponseUser.objects.all()
    serializer_class = ReponseUserSerializer






from rest_framework.permissions import IsAuthenticated
from .models import Questionnaire, Question, Reponse, Note, ReponseUser
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    questionnaire = QuestionnaireSerializer(read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class ReponseSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Reponse
        fields = ['id', 'question', 'reponse']


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = "__all__"
        permission_classes = [IsAuthenticated]



class ReponseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReponseUser
        fields = "__all__"
        permission_classes = [IsAuthenticated]
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ('user')




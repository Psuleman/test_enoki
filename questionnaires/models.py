from django.db import models
from qcm_project.settings import AUTH_USER_MODEL

# Create your models here.
# Question : id, id_questionnaire, question

class Questionnaire(models.Model):
    title=models.CharField(max_length=255)

    def __str__ (self):
        return self.title



class Question(models.Model):
    question= models.TextField()
    questionnaire= models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    def __str__ (self):
        return f"Qestionnaire : {self.questionnaire} | Question : {self.question}"


class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse = models.TextField()
    bonne_reponse = models.BooleanField(default=False)

    def __str__ (self):
        return f"{self.question} | Réponse : {self.reponse}"


class Note(models.Model):
    user=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    reponse_juste=models.BooleanField(default=False)

    def __str__ (self):
        return f"{self.user.username}"


class ReponseUser(models.Model):
    user=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    reponse = models.ManyToManyField(Reponse)
    estVrai=models.BooleanField()

    def __str__ (self):
        return f"{self.user.username}"
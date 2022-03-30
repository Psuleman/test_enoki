from django.contrib import admin
from questionnaires.models import Questionnaire, Question, Reponse, Note, ReponseUser
from data_seeder.admin import DataGeneratorAdmin
# Register your models here.
admin.site.register(Questionnaire, DataGeneratorAdmin)
admin.site.register(Question, DataGeneratorAdmin)
admin.site.register(Reponse, DataGeneratorAdmin)
admin.site.register(Note, DataGeneratorAdmin)
admin.site.register(ReponseUser, DataGeneratorAdmin)

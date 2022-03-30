from rest_framework import routers
from .views import NoteViewSet, ReponseUserViewSet, ReponseViewSet

router = routers.DefaultRouter()
router.register('api/note', NoteViewSet)
router.register('api/reponse-user', ReponseUserViewSet)

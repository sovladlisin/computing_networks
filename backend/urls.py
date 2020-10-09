from rest_framework import routers
from django.urls import path
from backend.api import ListViewSet, PersonViewSet, SystemViewSet, Markup_SystemViewSet, Markup_PersonViewSet

router = routers.DefaultRouter()
router.register('api/lists', ListViewSet, 'lists')
router.register('api/people', PersonViewSet, 'people')
router.register('api/systems', SystemViewSet, 'systems')
router.register('api/markup_system', Markup_SystemViewSet, 'markup_system')
router.register('api/markup_person', Markup_PersonViewSet, 'markup_person')

urlpatterns = router.urls

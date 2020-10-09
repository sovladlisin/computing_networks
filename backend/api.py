from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework import generics
from rest_framework.views import APIView, Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json

from backend.models import List, Person, System, Markup_System, Markup_Person
from backend.serializers import ListSerializer, PersonSerializer, Markup_PersonSerializer, SystemSerializer, Markup_SystemSerializer
# perm = permissions.IsAuthenticated
perm = permissions.AllowAny


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    permission_classes = [
        perm
    ]
    serializer_class = ListSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    permission_classes = [
        perm
    ]
    serializer_class = PersonSerializer


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    permission_classes = [
        perm
    ]
    serializer_class = SystemSerializer


class Markup_SystemViewSet(viewsets.ModelViewSet):
    queryset = Markup_System.objects.all()
    permission_classes = [
        perm
    ]
    serializer_class = Markup_SystemSerializer


class Markup_PersonViewSet(viewsets.ModelViewSet):
    queryset = Markup_Person.objects.all()
    permission_classes = [
        perm
    ]
    serializer_class = Markup_PersonSerializer

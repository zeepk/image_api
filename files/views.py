from django.shortcuts import render
from django.contrib.auth.models import TestModel
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import TestModelSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

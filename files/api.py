from files.models import TestModel
from rest_framework import viewsets
from files.serializers import TestModelSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
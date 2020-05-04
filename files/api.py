from files.models import TestModel, File, Image
from rest_framework import viewsets
from files.serializers import TestModelSerializer, FileSerializer, ImageSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class TestModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


class FileUploadView(viewsets.ModelViewSet):
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer

    queryset = File.objects.all()

class ImageUploadView(viewsets.ModelViewSet):
    # parser_class = (FileUploadParser,)
    serializer_class = ImageSerializer

    queryset = Image.objects.all()

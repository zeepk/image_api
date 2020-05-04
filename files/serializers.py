from .models import TestModel, File, Image
from rest_framework import serializers

class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel
        fields = ['question_text', 'pub_date']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
from django.contrib.auth.models import TestModel
from rest_framework import serializers

class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel
        fields = ['question_text', 'pub_date']
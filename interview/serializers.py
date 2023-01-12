from . import models
from .models import Category, QuestionAnswer
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class QuestionAnswerForDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionAnswer
        fields = '__all__'
        extra_kwargs = {
            'answer': {'write_only': True}
        }

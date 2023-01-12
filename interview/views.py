from django.db.models import Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import QuestionAnswerSerializer, CategorySerializer, QuestionAnswerForDetailSerializer
from .models import QuestionAnswer, Category
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework import filters


class QuestionAnswerPagePagination(PageNumberPagination):
    page_size = 3



class CategoryCreateApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerCreateApiView(generics.ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerForDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['question', 'category']
    ordering_fields = ['importance', ]
    pagination_class = QuestionAnswerPagePagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        question = self.request.query_params.get('question')
        if question and category:
            queryset = queryset.filter(Q(question__icontains=question) & Q(category=category))
        return queryset


class QuestionAnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer



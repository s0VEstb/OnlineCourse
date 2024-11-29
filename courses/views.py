from django.shortcuts import render
from .serializers import CourseSerializer, MounthSerializer, ClassAndHomeWorkSerializer
from .models import Course, Mounth, ClassAndHomeWork
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination



class CourseListAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']
    pagination_class = PageNumberPagination

    


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class MounthListAPIView(generics.ListCreateAPIView):
    queryset = Mounth.objects.all()
    serializer_class = MounthSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course']
    ordering_fields = ['name']
    pagination_class = PageNumberPagination


class MounthDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mounth.objects.all()
    serializer_class = MounthSerializer
    permission_classes = [IsAuthenticated]


class ClassAndHomeWorkListAPIView(generics.ListCreateAPIView):
    queryset = ClassAndHomeWork.objects.all()
    serializer_class = ClassAndHomeWorkSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['mounth', 'mounth__course']
    ordering_fields = ['mounth', 'mounth__course']
    pagination_class = PageNumberPagination


class ClassAndHomeWorkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassAndHomeWork.objects.all()
    serializer_class = ClassAndHomeWorkSerializer
    permission_classes = [IsAuthenticated]

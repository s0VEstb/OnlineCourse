from django.shortcuts import render
from .serializers import CourseSerializer, MounthSerializer, ClassAndHomeWorkSerializer
from .models import Course, Mounth, ClassAndHomeWork
from rest_framework import generics


class CourseListAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class MounthListAPIView(generics.ListCreateAPIView):
    queryset = Mounth.objects.all()
    serializer_class = MounthSerializer


class MounthDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mounth.objects.all()
    serializer_class = MounthSerializer


class ClassAndHomeWorkListAPIView(generics.ListCreateAPIView):
    queryset = ClassAndHomeWork.objects.all()
    serializer_class = ClassAndHomeWorkSerializer


class ClassAndHomeWorkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassAndHomeWork.objects.all()
    serializer_class = ClassAndHomeWorkSerializer

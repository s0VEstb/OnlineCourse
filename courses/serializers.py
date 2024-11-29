from .models import Course, Mounth, ClassAndHomeWork
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description')


class MounthSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Mounth
        fields = ('id', 'name', 'course')


class ClassAndHomeWorkSerializer(serializers.ModelSerializer):
    mounth = MounthSerializer()
    class Meta:
        model = ClassAndHomeWork
        fields = ('id', 'title', 'description', 'video', 'homework', 'mounth')
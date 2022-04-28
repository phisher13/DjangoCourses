from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'type', 'category', 'price')


class CourseDetailSerializer(serializers.ModelSerializer):
    students_quantity = serializers.IntegerField(source='students.count', read_only=True)

    class Meta:
        model = Course
        exclude = ('students',)


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('students',)

from django.test import TestCase

from ..models import Course
from ..serializers import (
    CourseSerializer,
    CourseDetailSerializer,
    CourseCreateSerializer)


class CourseSerializerTestCase(TestCase):
    def test_serializer(self):
        course = Course.objects.create(title='Test-Title',
                                       slug='test-slug',
                                       description='test-description',
                                       type='online',
                                       price=200,
                                       category='programming')
        course_all = Course.objects.all()
        data = CourseSerializer(course_all, many=True).data
        expected_data = [
            {
                'title': course.title,
                'type': course.type,
                'category': course.category,
                'price': course.price
            }
        ]

        self.assertEqual(expected_data, data)


class CourseDetailSerializerTestCase(TestCase):
    def test_detail_serializer(self):
        course = Course.objects.create(title='Test-Title',
                                       slug='test-slug',
                                       description='test-description',
                                       type='online',
                                       price=200,
                                       category='programming')

        data = CourseDetailSerializer(course).data
        expected_data = {
            'students_quantity': course.students.count(),
            'title': course.title,
            'slug': course.slug,
            'description': course.description,
            'type': course.type,
            'price': course.price,
            'category': course.category,
        }

        self.assertEqual(expected_data, data)


class CourseCreateSerializerTestCase(TestCase):
    def test_create_serializer(self):
        course = Course.objects.create(title='Test-Title',
                                       slug='test-slug',
                                       description='test-description',
                                       type='online',
                                       price=200,
                                       category='programming')

        data = CourseCreateSerializer(course).data
        expected_data = {
            'title': course.title,
            'slug': course.slug,
            'description': course.description,
            'type': course.type,
            'price': course.price,
            'category': course.category,
        }

        self.assertEqual(expected_data, data)

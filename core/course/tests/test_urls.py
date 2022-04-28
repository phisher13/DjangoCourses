from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from ..models import Course
from ..serializers import CourseSerializer


def get_token_by_login(self):
    User.objects.create_superuser(username='admin',
                                  password='admin',
                                  email='admin@admin.com')
    data = {
        'username': 'admin',
        'password': 'admin'
    }
    response = self.client.post('http://localhost:8000/api/token/', data=data)

    return response.data['access']


class CourseApiTestCase(APITestCase):
    def test_get(self):
        Course.objects.create(title='Test-Title',
                              slug='test-slug',
                              description='test-description',
                              type='online',
                              price=200,
                              files=SimpleUploadedFile('test.txt', b'test-content'),
                              category='programming')
        course_all = Course.objects.all()
        url = reverse('course')
        response = self.client.get(url)
        serializer_data = CourseSerializer(course_all, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_post(self):
        data = {
            'title': 'test-title',
            'slug': 'test-slug',
            'description': 'test-description',
            'type': 'online',
            'price': 1999,
            'files': SimpleUploadedFile('test.txt', b'test-content'),
            'category': 'programming',
        }
        client = RequestsClient()
        response = client.post('http://localhost:8000/api/v1/course/new/',
                               data=data,
                               headers=({"Authorization": f"Bearer {get_token_by_login(self=self)}"})
                               )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_put(self):
        course = Course.objects.create(title='Test-Title',
                                       slug='test-slug',
                                       description='test-description',
                                       type='online',
                                       price=200,
                                       category='programming')
        data = {
            'title': 'test-upd-title',
            'slug': 'test-upd-slug',
            'description': 'test-upd-description',
            'type': 'online',
            'price': 3999,
            'category': 'programming',
        }

        client = RequestsClient()
        response = client.put(f'http://localhost:8000/api/v1/course/update/{course.slug}/',
                              data=data,
                              headers={'Authorization': f"Bearer {get_token_by_login(self)}"}
                              )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete(self):
        course = Course.objects.create(title='Test-Title',
                                       slug='test-slug',
                                       description='test-description',
                                       type='online',
                                       price=200,
                                       category='programming')
        client = RequestsClient()
        response = client.delete(f'http://localhost:8000/api/v1/course/delete/{course.slug}/',
                                 headers={'Authorization': f"Bearer {get_token_by_login(self)}"}
                                 )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_join_student_to_course(self):
        course = Course.objects.create(title='Test-Title',
                                       slug='test-slug',
                                       description='test-description',
                                       type='online',
                                       price=200,
                                       category='programming')
        client = RequestsClient()
        response = client.post(f'http://localhost:8000/api/v1/course/join/{course.slug}/',
                               headers={'Authorization': f"Bearer {get_token_by_login(self)}"}
                               )
        get_course = Course.objects.get(slug=course.slug)

        self.assertEqual(get_course.students.count(), 1)

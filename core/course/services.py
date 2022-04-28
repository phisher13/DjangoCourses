from django.db.models import Count
from django.http import FileResponse
from rest_framework.views import Response

from .models import Course
from .serializers import CourseSerializer


def request_without_parameter():
    queryset = Course.objects.all()
    serializer = CourseSerializer(queryset, many=True)
    return Response(serializer.data)


def sort_by_price(request):
    parameter = request.GET.get('price')

    if parameter in ['lowest', 'lowest/']:
        queryset = Course.objects.order_by('price')
    elif parameter in ['highest', 'highest/']:
        queryset = Course.objects.order_by('-price')
    else:
        queryset = Course.objects.all()

    serializer = CourseSerializer(queryset, many=True)

    return Response(serializer.data)


def sort_by_popularity(request):
    parameter = request.GET.get('popularity')

    if parameter in ['up', 'up/']:
        queryset = Course.objects.annotate(quantity=Count('students'))\
                                    .order_by('quantity')

    elif parameter in ['down', 'down/']:
        queryset = Course.objects.annotate(quantity=Count('students'))\
                                    .order_by('-quantity')
    else:
        queryset = Course.objects.values('title', 'type', 'category', 'price')

    serializer = CourseSerializer(queryset, many=True)

    return Response(serializer.data)


def sort_by_parameter(request):
    request_parameter = request.GET
    for parameter in request_parameter:
        if parameter == 'price':
            return sort_by_price(request)
        elif parameter == 'popularity':
            return sort_by_popularity(request)
    return request_without_parameter()


def choose_student_by_id(request):
    queryset = Course.objects.filter(students__id=request.user.pk)
    serializer = CourseSerializer(queryset, many=True)
    return Response(serializer.data)


def join_student(request, slug):
    course = Course.objects.get(slug=slug)
    if request.user in course.students.all():
        return Response({'error': f"Student: '{request.user.username}' already joined to course: '{course.title}'"})
    course.students.add(request.user.pk)
    return Response({'success': f"Student: '{request.user.username}' joined to course: '{course.title}'"})


def download_files(request, slug):
    courses = Course.objects.filter(slug=slug).prefetch_related('students')
    for course in courses:
        if request.user in course.students.all():
            return FileResponse(
                open(course.files.path, 'rb'), filename=str(course.files.name), as_attachment=True
            )
        return Response({'error': "You can't download a files, because you didn't join to this course"})


def remove_student(request, slug):
    course = Course.objects.get(slug=slug)
    if request.user in course.students.all():
        course.students.remove(request.user.pk)
        return Response({'success': f"Student: '{request.user.username}' was removed from course: '{course.title}'"})
    return Response({'error': f"Student: '{request.user.username}' didn't join to course: '{course.title}'"})

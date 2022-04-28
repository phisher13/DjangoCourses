from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.viewsets import ViewSet

from .serializers import CourseSerializer, CourseCreateSerializer, CourseDetailSerializer
from .models import Course
from .services import (
    sort_by_parameter,
    choose_student_by_id,
    join_student,
    remove_student,
    download_files)


class CourseListView(ViewSet):
    """don't forget about docs string"""

    @staticmethod
    def sort_course_by_request_parameter(request):
        return sort_by_parameter(request)


class UserCourses(ViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def students_courses(request):
        return choose_student_by_id(request)


class JoinStudentToCourse(ViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def join_student_to_course(request, slug):
        return join_student(request, slug)


class DownloadCoursesFile(ViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def download_courses_file(request, slug):
        return download_files(request, slug)


class RemoveStudentFromCourse(ViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def remove_student_from_course(request, slug):
        return remove_student(request, slug)


class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'slug'


class CourseCreateView(CreateAPIView):
    serializer_class = CourseCreateSerializer
    permission_classes = [IsAdminUser]


class CourseUpdateView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'


class CourseDestroyView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'

from django.urls import path

from . import views

urlpatterns = [
    path('course/', views.CourseListView.as_view({'get': 'sort_course_by_request_parameter'}), name='course'),
    path('course/detail/<str:slug>/', views.CourseDetailView.as_view()),
    path('course/my-courses/', views.UserCourses.as_view({'get': 'students_courses'})),
    path('course/new/', views.CourseCreateView.as_view()),
    path('course/join/<str:slug>/', views.JoinStudentToCourse.as_view({'post': 'join_student_to_course'})),
    path('course/download/<str:slug>/', views.DownloadCoursesFile.as_view({'get': 'download_courses_file'})),
    path('course/remove/<str:slug>/', views.RemoveStudentFromCourse.as_view({'post': 'remove_student_from_course'})),
    path('course/update/<str:slug>/', views.CourseUpdateView.as_view()),
    path('course/delete/<str:slug>/', views.CourseDestroyView.as_view()),
]

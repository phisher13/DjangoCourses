from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'description', 'price', 'type', 'category', 'date', 'students_quantity')

    @staticmethod
    def students_quantity(obj):
        return obj.students.all().count()

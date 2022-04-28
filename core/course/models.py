from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('online', 'ONLINE'),
    ('offline', 'OFFLINE')
)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'categories'
        ordering = ['id']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    description = models.TextField()
    type = models.CharField(choices=TYPE_CHOICES,
                            default='online',
                            null=False,
                            max_length=255
                            )
    price = models.IntegerField()
    files = models.FileField(upload_to=f'courses/{title.name}')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course'
        ordering = ['date']
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.title

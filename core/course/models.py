from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('online', 'ONLINE'),
    ('offline', 'OFFLINE')
)

CATEGORY_CHOICES = (
    ('programming', 'PROGRAMMING'),
    ('games', 'GAMES'),
    ('design', 'DESIGN'),
    ('marketing', 'MARKETING')
)


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
    category = models.CharField(choices=CATEGORY_CHOICES,
                                default=None,
                                null=False,
                                max_length=255)
    students = models.ManyToManyField(User, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course'
        ordering = ['date']
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.title

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    admission_number = models.CharField(
        max_length=20,
        unique=True
    )
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admission_number} - {self.name}"

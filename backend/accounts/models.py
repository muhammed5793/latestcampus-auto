from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('PROFESSOR', 'Professor'),
        ('STUDENT', 'Student'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    admission_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

from django.db import models
from students.models import Student

class Marks(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='marks'
    )
    subject = models.CharField(max_length=100)
    marks_percentage = models.FloatField()

    def __str__(self):
        return f"{self.student.admission_number} - {self.subject}"
class PerformanceReport(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='performance_report'
    )
    attendance_percentage = models.FloatField()
    marks_percentage = models.FloatField()
    performance_score = models.FloatField()
    risk_flag = models.BooleanField(default=False)
    generated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.admission_number} - {self.performance_score}"

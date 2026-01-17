from celery import shared_task
from students.models import Student
from .services import generate_performance_report
from .models import PerformanceReport
from .alerts import send_risk_alert

@shared_task
def generate_all_performance_reports():
    for student in Student.objects.all():
        generate_performance_report(student)

@shared_task
def send_risk_alerts():
    reports = PerformanceReport.objects.filter(risk_flag=True)

    for report in reports:
        send_risk_alert(report.student, report)
from attendance.models import Attendance
from students.models import Student
from .models import PerformanceReport, Marks

ATTENDANCE_THRESHOLD = 75

def calculate_attendance_percentage(student):
    total_days = Attendance.objects.filter(student=student).count()
    if total_days == 0:
        return 0
    return 100  # Since we mark only PRESENT currently

def calculate_marks_percentage(student):
    marks = Marks.objects.filter(student=student)
    if not marks.exists():
        return 0
    return sum(m.marks_percentage for m in marks) / marks.count()

def generate_performance_report(student):
    attendance_pct = calculate_attendance_percentage(student)
    marks_pct = calculate_marks_percentage(student)

    performance_score = (attendance_pct * 0.4) + (marks_pct * 0.6)
    risk_flag = attendance_pct < ATTENDANCE_THRESHOLD

    report, _ = PerformanceReport.objects.update_or_create(
        student=student,
        defaults={
            "attendance_percentage": attendance_pct,
            "marks_percentage": marks_pct,
            "performance_score": performance_score,
            "risk_flag": risk_flag,
        }
    )
    return report

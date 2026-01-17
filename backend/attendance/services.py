from datetime import date
from students.models import Student
from .models import Attendance

CONFIDENCE_THRESHOLD = 0.60

def mark_attendance(admission_number, confidence):
    """
    Auto-mark attendance for a student if not already marked today
    """

    if confidence < CONFIDENCE_THRESHOLD:
        return {
            "status": "ignored",
            "reason": "Low confidence"
        }

    try:
        student = Student.objects.get(admission_number=admission_number)
    except Student.DoesNotExist:
        return {
            "status": "failed",
            "reason": "Student not found"
        }

    today = date.today()

    attendance, created = Attendance.objects.get_or_create(
        student=student,
        date=today,
        defaults={
            "status": "PRESENT",
            "confidence_score": confidence
        }
    )

    if not created:
        return {
            "status": "exists",
            "message": "Attendance already marked"
        }

    return {
        "status": "success",
        "student": student.admission_number,
        "confidence": confidence
    }

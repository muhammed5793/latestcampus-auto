from django.core.mail import send_mail

def send_risk_alert(student, report):
    subject = "⚠ Academic Risk Alert"
    message = f"""
Hello {student.name},

You are currently marked as AT RISK.

Attendance: {report.attendance_percentage}%
Marks: {report.marks_percentage}%
Performance Score: {report.performance_score}

Please contact your department for guidance.
"""
    send_mail(
        subject,
        message,
        'aboobackerkv598@gmail.com',
        [student.email],
        fail_silently=False
    )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from students.models import Student
from performance.models import PerformanceReport
from django.db.models import Avg
from students.models import Student

class StudentDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student = Student.objects.get(user=request.user)
        report = PerformanceReport.objects.get(student=student)

        return Response({
            "admission_number": student.admission_number,
            "attendance_percentage": report.attendance_percentage,
            "marks_percentage": report.marks_percentage,
            "performance_score": report.performance_score,
            "at_risk": report.risk_flag,
        })
class ProfessorDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "PROFESSOR":
            return Response({"error": "Forbidden"}, status=403)

        reports = PerformanceReport.objects.filter(risk_flag=True)

        data = [{
            "admission_number": r.student.admission_number,
            "performance_score": r.performance_score,
        } for r in reports]

        return Response({"at_risk_students": data})

class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "ADMIN":
            return Response({"error": "Forbidden"}, status=403)

        return Response({
            "total_students": Student.objects.count(),
            "average_performance": PerformanceReport.objects.aggregate(
                avg=Avg("performance_score")
            )["avg"]
        })

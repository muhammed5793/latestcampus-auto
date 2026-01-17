from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # 🔐 this authenticates username & password
        data = super().validate(attrs)

        # ➕ add custom fields to response
        data["username"] = self.user.username
        data["role"] = self.user.role
        data["admission_number"] = self.user.admission_number

        return data

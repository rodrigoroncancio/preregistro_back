from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAdminUser

from core.models import Staff, UserPNIS
from core.serializers.staff import UserPNISSerializer
from rest_framework.viewsets import ViewSet

class UserAPIView(APIView):

    def get(self, request):

        user = request.user
        if user.is_anonymous:
            return Response({"message": "Unauthorized"}, status=401)

        if not user.is_staff:
            return Response({"message": "Staff not found"}, status=404)

        staff = Staff.objects.filter(user=user).first()
        if not staff:
            return Response({"message": "Staff not found"}, status=404)
        roles = user.roles.all()
        array_roles = []
        for rol in roles:
            array_roles.append({"id": rol.rol_id, "nombre": rol.rol.nombre})

        data = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": 1 if user.is_superuser else (2 if user.is_staff else 3),
            "roles": array_roles,
            "image": staff.image if staff else "",
            "phone": staff.phone if staff else "",
        }

        return Response(data)


    
    
class UserPnisA2PIView(APIView):

    def get(self, request):

        user = request.user
        if user.is_anonymous:
            return Response({"message": "Unauthorized"}, status=401)

        if not user.is_staff:
            return Response({"message": "Staff not found"}, status=404)

        staff = Staff.objects.filter(user=user).first()
        if not staff:
            return Response({"message": "Staff not found"}, status=404)

        data = {
            "Id": user.id,
            "Name": user.first_name,
            "Lastname": user.last_name
        }

        return Response(data)

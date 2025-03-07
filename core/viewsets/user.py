from rest_framework.response import Response
from core.models import Staff, Rol
from rest_framework import viewsets

class UserViewSet(viewsets.GenericViewSet):

    def user_data(self, request):
        user = request.user
        if user.is_anonymous:
            return Response({"message": "Unauthorized"}, status=401)
        staff = Staff.objects.filter(user=user).first()
        roles = user.roles.all()
        array_roles = []
        if user.is_superuser:
            array_roles.append({"id": 1, "nombre": "Admin"})
        for rol in roles:
            if rol.rol_id == 1:
                continue
            else:
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
    
    def roles(self, request):
        lista = []
        for rol in Rol.objects.all():
            lista.append({"id": rol.id, "label": rol.nombre})
        return Response(lista)


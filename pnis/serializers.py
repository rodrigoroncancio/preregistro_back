from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

class PnisTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_payload(attrs)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data

    def get_payload(self, attrs):
        refresh = self.get_token(self.user)
        roles = self.user.roles.all()
        array_roles = []
        for rol in roles:
            array_roles.append(rol.rol_id)
        refresh["roles"] = array_roles
        return refresh
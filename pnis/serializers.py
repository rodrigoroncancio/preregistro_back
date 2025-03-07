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
        """
        Generate a JWT payload with user's roles.

        This function retrieves the user's roles from the database, checks if the user is a superuser,
        and adds the roles to the JWT payload.

        Parameters:
        attrs (dict): A dictionary containing user attributes.

        Returns:
        dict: A dictionary representing the JWT payload with user's roles.
        """
        refresh = self.get_token(self.user)
        roles = self.user.roles.all()
        array_roles = []
        if self.user.is_superuser:
            array_roles.append(1)
        for rol in roles:
            if rol.rol_id not in array_roles:
                array_roles.append(rol.rol_id)
        refresh["roles"] = array_roles
        return refresh
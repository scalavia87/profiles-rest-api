from rest_framework import serializers
from profiles_api import models

"""SIRVEN PARA VALIDAR LOS DATOS QUE LE METEMOS A LOS POST, PUT Y PATCH"""
"""TAMBIÉN SON LOS CAMPOS QUE APARECERÁN CUANDO PROBEMOS LA API EN EL NAVEGADOR. POR EJEMPLO name"""

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    # Aqui estamos haciendo override al metodo create estandar de ModelSerializer
    def create(self, validated_data):
        """Create and return a new user"""
        ## ESTAMOS LLAMANDO A LA FUNCION create_user de la clase UserProfile
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

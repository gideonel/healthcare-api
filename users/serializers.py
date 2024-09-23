from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'firstname', 'lastname', 'address', 'email', 'phone', 'is_doctor')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'firstname', 'lastname', 'address', 'email', 'phone', 'is_doctor')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            firstname=validated_data.get('firstname', ''),
            lastname=validated_data.get('lastname', ''),
            address=validated_data.get('address', ''),
            email=validated_data['email'],
            phone=validated_data.get('phone', ''),
            is_doctor=validated_data.get('is_doctor', False)
        )
        return user
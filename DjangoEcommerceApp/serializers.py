from rest_framework import serializers
from .models import CustomUser, AdminUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'user_type']  # Add any other fields you want to include
        # You might want to exclude sensitive fields like 'password' from the serializer,
        # or handle them with care if you need to include them for any reason.

class AdminUserSerializer(serializers.ModelSerializer):
    auth_user_id = CustomUserSerializer()  # This will include the CustomUser details in the serialized data
    
    class Meta:
        model = AdminUser
        fields = ['id', 'profile_pic', 'auth_user_id', 'created_at']
        # Depending on your requirements, you might need to customize the handling of the FileField in the serializer.

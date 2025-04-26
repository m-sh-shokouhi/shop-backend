from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ["username","password1","password2","email"]
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def validate(self,attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"] # TODO: email uniqueness must be checked before save.
        )

        user.set_password(validated_data["password1"])
        user.save()
        return user
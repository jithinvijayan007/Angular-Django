from rest_framework import serializers
from testapp.models import UserDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ("vchr_name","vchr_address","vchr_gender")

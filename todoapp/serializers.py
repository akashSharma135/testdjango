from rest_framework import serializers
from .models import ManagerAssigned, NewUser

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'
        
        
class ManagerAssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerAssigned
        fields = ['id', 'manager', 'user']
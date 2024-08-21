from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import serializers

from .models import Accounts


class RegisterSerializer(serializers.Serializer):
    '''
        Schema for Account Model
    '''
    email = serializers.EmailField()
    name = serializers.CharField()
    address = serializers.CharField()
    phone_no = serializers.IntegerField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        '''
            Handles the validation for the email and password
        '''
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Password didnot match.")
        
        if Accounts.objects.filter(email = data.get('email')).exists():
            raise serializers.ValidationError("Email is already used.")
        
        return data
    

    @transaction.atomic
    def save(self):
        try:
            user = Accounts.objects.create(
                email = self.validated_data['email'],
                name = self.validated_data['name'],
                address = self.validated_data['address'],
                phone_no = self.validated_data['phone_no'],
                password = make_password(self.validated_data['confirm_password'])
            )
        except Exception as e:
            raise e 
        
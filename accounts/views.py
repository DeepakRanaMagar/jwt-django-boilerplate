from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import RegisterSerializer


class RegistrationView(APIView):
    '''
        Endpoint to handle the user registration
    '''
    
    def post(self, request):
        
        data  = request.data 

        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {
                        "success": "Account successfully created."
                    }, status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {
                        "error": str(e)
                    }, status= status.HTTP_400_BAD_REQUEST
                )

class LoginView(APIView):
    '''
        Endpoint to handle the user login
    '''
    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        
        logged_in = authenticate(request, email=email, password=password)
        
        if logged_in:
            print("Authentication successful")

        return Response('check terminal')
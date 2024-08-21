from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class Home(APIView):
    '''
        Endpoint for basic response
    '''
    permission_classes = [IsAuthenticated, ]
    
    def get(self, request):
        
        content = {
            'congratulations':"You've have learned implementation of JWT authentication." 
        }

        return Response(content)

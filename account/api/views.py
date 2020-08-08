from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.api.serializers import RegistrationSerializer


@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data["respomse"] = "User registered successfully"
        data['email'] = account.email
        data['username'] = account.username
    else:
        data = serializer.errors
    return Response(data)
    

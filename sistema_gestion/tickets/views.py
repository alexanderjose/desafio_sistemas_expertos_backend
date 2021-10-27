from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Ticket
from .serializers import TicketSerializer
from .serializers import CustomObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
import jwt
import os


class CustomTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomObtainPairSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def listado_tickets(request):
    """
    TODO: comments
    """

    if request.method == 'GET':
        tickets = Ticket.objects.all()
        authorization_header = request.headers.get('Authorization')
        access_token = authorization_header.split(' ')[1]
        payload = jwt.decode(
                access_token, os.getenv('SECRET'), algorithms=['HS256']
        )
        is_admin = User.objects.filter(
            username=payload['username'], groups__name='administrador'
        ).exists()
        serializer = TicketSerializer(tickets, many=True)
        data = {
            'is_admin': is_admin,
            'data': serializer.data
        }
        return JsonResponse(data, status=200, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

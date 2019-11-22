from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
# Create your views here.


@api_view(['POST'])
def signup(request):
    pass

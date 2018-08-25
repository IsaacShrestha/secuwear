from django.shortcuts import render
from .models import *
from .serializers import *

#import from rest_framework
from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.

def home(request):
	return render(request, 'index.html', {})

class CollectedDataViewSet(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	queryset = CollectedData.objects.all()
	serializer_class = CollectedDataSerializer
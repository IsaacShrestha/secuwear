from rest_framework import serializers
from .models import *


class CollectedDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CollectedData
		fields = ('time', 'temperature')
from rest_framework import serializers


from django.db.models import fields
from rest_framework import serializers
from .models import Item

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'name', 'id')



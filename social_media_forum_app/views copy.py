from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models as md
from . import serializers as sz
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


@api_view
def login(request):
	# initializing a login 
	pass

@api_view
def signin(request):
	# on final of this, create a new user 
	ct_u()
	pass

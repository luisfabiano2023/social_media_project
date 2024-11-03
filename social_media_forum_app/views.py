from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

@api_view(['GET'])
def show(request):
	# only shows if the server still running

	return Response(show)

@api_view(['POST'])
def ct_u(request):
	# create a new fella on this forum

	return Response(ct_u)

@api_view(['GET'])
def dt_u(request):
	# delete a previous added fella

	return Response(dt_u)

@api_view(['GET'])
def ls_u(request):
	# finalizing this crud

	return Response(ls_u)

@api_view
def login(request):
	# initializing a login 
	pass

@api_view
def signin(request):
	# on final of this, create a new user 
	ct_u()
	pass
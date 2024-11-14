from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers as sz,models as md,views as vi
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User



def login():
	pass

def signup():
	method='POST'
	
	pass

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models as md
from . import serializers as sz
from rest_framework import status
from . import views


@api_view("GET")
def check():
    dados=views.ct_u.data
    return dados







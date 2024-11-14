from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models as md
from . import serializers as sz
from rest_framework import status

@api_view(['GET'])
def show(request):
 return render(request,'sm-app/index.html')

@api_view(['POST'])
def ct_u(request):
	users=sz.UserSerializer(data=request.data)
	if md.User.objects.filter(**request.data).exists():
		raise sz.serializers.ValidationError("erro,usuario com nome já sendo utilizado,por favor troque as informações ")
	if users.is_valid():
		users.save()
		return Response(users.data)
      
@api_view(['GET'])
def dt_u(request):
	# delete a previous added fella

	return Response(dt_u)

@api_view(['GET'])
def ls_u(request):
    if request.query_params:
        items = md.User.objects.filter(**request.query_params.dict())
    else:
        items = md.User.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = sz.UserSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


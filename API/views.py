from django.shortcuts import render, get_object_or_404
from django.http import request, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import PrzewozSerializer
from . models import Przewoz
# Create your views here.


class PrzewozID(APIView):

    def get(self, request, id=None):
        przewoz = get_object_or_404(Przewoz, pk=id)
        serializerPrzewoz = PrzewozSerializer(przewoz)

        if id:
            return Response(serializerPrzewoz.data, status=status.HTTP_200_OK)
        return Response(serializerPrzewoz.errors, status=status.HTTP_404_NOT_FOUND)


class Przewozy(APIView):

    def get(self, request):

        przewozy = Przewoz.objects.all()
        serializer = PrzewozSerializer(przewozy, many=True)

        if serializer :
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):

        serializer = PrzewozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
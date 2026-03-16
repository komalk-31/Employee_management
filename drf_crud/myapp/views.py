from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView #rest_framework.views APIview used to create views
from rest_framework.response import Response #rest_framework.respoce used to return responce
from .models import Employee #importing Employee model from models.py
from .serializers import EmployeeSerializer #importing EmployeeSerializer from serializers.py
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


class EmployeeList(APIView):

    def get(self, request, pk=None):

        if pk:
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data)
    
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeDetail(APIView):

    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
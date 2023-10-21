from django.shortcuts import render
from rest_framework.response import Response
from viewset_view.models import Student
from rest_framework import status
from rest_framework import viewsets
from viewset_view.serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            std = Student.objects.get(id=id)
            serializer = StudentSerializer(std)
            return Response(serializer.data)

    def create(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, format=None):
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'})
        return Response(serializer.errors)

    def partial_update(self, request, pk, format=None):
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk, format=None):
        id = pk
        std = Student.objects.get(pk=id)
        std.delete()
        return Response({'msg': 'data deleted'})

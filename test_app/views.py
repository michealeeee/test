from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.
class CreateUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': 'created a new user',
                    'user': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetUserAPIView(APIView):
    def get(self,request,name):
        try:
            s = User.objects.get(name=name)
            serialized_data = UserSerializer(s)
            return Response(serialized_data.data,status = 200)
        except User.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
        
class GetAllUserAPIView(APIView):
    def get(self,request):
        try:
            s = User.objects.all()
            serialized_data = UserSerializer(s,many=True)
            return Response(serialized_data.data,status = 200)
        except User.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
        
class DeleteUserAPIView(APIView):
    def delete(self,request,name):
        try:
            s = User.objects.get(name=name)
            s.delete()
            return Response({'success':'user deleted successfully'},status = 200)
        except User.DoesNotExist:
            return Response(
    {'error': 'user not found'},status=status.HTTP_404_NOT_FOUND)
        

        


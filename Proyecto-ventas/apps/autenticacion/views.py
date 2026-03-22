from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer


class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.validated_data['user']

            return Response({
                "mensaje": "Login exitoso",
                "usuario": user.username,
                "rol": user.rol
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

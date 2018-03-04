from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# from django.template import RequestContext

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .forms import UserForm, LoginForm
from .serializers import (
    UserLoginSerializer,
)

import jwt
import time

JWT_SECRET = "mysecretkey"

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('memo_list')
    else:
        form = UserForm()
        return render(request, 'auth_jwt/join.html', {'form': form})

def signin(request):
    if request.method == "POST":
        # form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('memo_list')
            else:
                return HttpResponse('유효한 계정이 아닙니다. 다시 시도 해보세요.')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'auth_jwt/login.html', {'form': form})

# class UserCreateAPIView():

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")

        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        # username = request.data['username']
        # password = request.data['password']
        #
        # try:
        #     # user = User.objects.get(username=username, password=password)
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     return Response({'Error': "Invalid username/password"}, status="400")
        #
        # if user and user.check_password(password):
        #     expire_ts = int(time.time()) + 3600
        #     payload = {
        #         'username': username,
        #         'expire': expire_ts,
        #     }
        #
        #     token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
        #
        #     # jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
        #
        #     # login(request, user)
        #     # return redirect('memo_list')
        #     # return HttpResponse(
        #     #     # json.dumps(jwt_token),
        #     #     token,
        #     #     status=200,
        #     #     content_type="application/json"
        #     # )
        #     return Response(token)
        #     # return Response(user, status=HTTP_200_OK)
        #     # return HttpResponse(user, status=HTTP_200_OK)
        # else:
        #     return Response(
        #         {'Error': "Invalid user"},
        #         status=400,
        #         content_type="application/json"
        #     )

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'auth_jwt/login.html', {'form': form})
# from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.http import HttpResponseRedirect, HttpResponse

import logging

logging.basicConfig(filename='./test.log', level=logging.DEBUG)

@csrf_exempt
def login(request):

    if request.POST:
        #print(request.POST.get('userId',None))
        if 'login-id-val' in request.POST:
            userModel = models.UserCount.objects.filter(
                userId=request.POST.get('login-id-val', None),
                userPw=request.POST.get('login-pw-val', None))

            if userModel.exists():
                request.session['login-id-val'] = request.POST.get('login-id-val')
                print("아이디, 비번 일치 - session save id")
                return render(request, "onePage/main.html")
            else:
                print("정보 없음")
                return render(request, "onePage/index.html")
    

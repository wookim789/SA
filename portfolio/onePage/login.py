# from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.http import HttpResponseRedirect, HttpResponse

# from django.http import HttpRequest
# from django.http import HttpResponse
import logging


logging.basicConfig(filename='./test.log', level=logging.DEBUG)

@csrf_exempt
def login(request):

    #  models.SelectDate.objects.filter(userId=request.POST['user_ID'],
    #                                            selectDate=request.POST["selectDate"])
    #print(request.POST.get('userId'))

    if request.POST:
        if 'userName' in request.POST:
            userId = request.POST.get('userName', None)
            userModel = models.UserCount.objects.filter(
                userId=request.POST.get('userId', None),
                userPw=request.POST.get('userPw', None))
            print(userId)
            if userModel.exists():
                request.session['userName'] = request.POST.get('userName')  
                print(userModel['userPw'])
    return Response(request)

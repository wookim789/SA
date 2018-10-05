# from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
import logging

logging.basicConfig(filename='./test.log', level=logging.DEBUG)
# Create your views here.


def index(request):
    logging.debug(
        "index***********************************************************************")
    return render(request, 'onePage/index.html')


@csrf_exempt
def getMemberId(request):
    logging.debug(
        "getMemebID***********************************************************************")
    model = models.SelectDate.objects.all()
    result = []
    logging.debug(request)

    for i in model:
        result.append({"userId": i.userId,
                       "selectDate": i.selectDate,
                       "dateCount": i.dateCount,
                       "confirmIndicator": i.confirmIndicator})
    logging.debug(result)
    return JsonResponse(result, safe=False)


@csrf_exempt
def loadCalendar(request):
    model = models.SelectDate.objects.all()
    result = []
    j = 0
    for i in model:
        if result == []:
            result.append({"userId": i.userId,
                           "selectDate": i.selectDate,
                           "dateCount": i.dateCount,
                           "confirmIndicator": i.confirmIndicator})
            j += 1
        elif i.selectDate != result[j-1]['selectDate']:
            result.append({"userId": i.userId,
                           "selectDate": i.selectDate,
                           "dateCount": i.dateCount,
                           "confirmIndicator": i.confirmIndicator})
            j += 1
    logging.debug(result)
    return JsonResponse(result, safe=False)


def selectCalendar(request):
    beModel = models.SelectDate.objects.filter(
        SelectDate=request['selectDate'])
    for i in beModel:
        cnt = i.dateCount + 1
        break
    model = models.SelectDate(userId=request.userId,
                              selectDate=request.date,
                              dateCount=cnt,
                              confirmIndicator=0)
    model.save()
    beModel.objects.all().update(dateCount=cnt)

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


@csrf_exempt
def selectCalendar(request):
    # logging.debug(request)
    logging.debug(request.POST['selectDate'])
    logging.debug(request.POST.get('user_ID'))

    beModel = models.SelectDate.objects.filter(
        selectDate=request.POST['selectDate'])

    cnt = 0
    for i in beModel:
        cnt = i.dateCount + 1
        break
    if cnt == 0:
        cnt = 1
    model = models.SelectDate(userId=request.POST.get('user_ID'),
                              selectDate=request.POST['selectDate'],
                              dateCount=cnt,
                              confirmIndicator=0)
    model.save()
    beModel.update(dateCount=cnt)
    answer = {"requset": True}
    return JsonResponse(answer)

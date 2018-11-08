# from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
import logging

logging.basicConfig(filename='./test.log', level=logging.DEBUG)
# Create your views here.

#logging.debug(result)


def index(request):
    return render(request, 'onePage/index.html')


@csrf_exempt
def getMemberId(request):
    model = models.SelectDate.objects.all()
    result = []

    for i in model:
        result.append({"userId": i.userId,
                       "selectDate": i.selectDate,
                       "dateCount": i.dateCount,
                       "confirmIndicator": i.confirmIndicator})

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
    return JsonResponse(result, safe=False)


@csrf_exempt
def selectCalendar(request):
    bemodel = models.SelectDate.objects.filter(userId=request.POST['user_ID'],
                                               selectDate=request.POST["selectDate"])
    logging.debug(bemodel)
    if not bemodel.exists():
        bemodel = models.SelectDate.objects.filter(
            selectDate=request.POST['selectDate'])
        cnt = 0
        for i in bemodel:
            cnt = i.dateCount + 1
            break
        if cnt == 0:
            cnt = 1
        model = models.SelectDate(userId=request.POST.get('user_ID'),
                                  selectDate=request.POST['selectDate'],
                                  dateCount=cnt,
                                  confirmIndicator=0)
        model.save()
        bemodel.update(dateCount=cnt)
        answer = {"requset": True}
    else:
        cnt = bemodel[0].dateCount - 1
        bemodel = models.SelectDate.objects.filter(userId=request.POST["user_ID"],
                                                   selectDate=request.POST["selectDate"]).delete()
        bemodel = models.SelectDate.objects.filter(
            selectDate=request.POST["selectDate"])
        bemodel.update(dateCount=cnt)

        answer = {"requset": "삭제"}
    return JsonResponse(answer)


@csrf_exempt
def fixcal(request):
    bemodel = models.SelectDate.objects.filter(selectDate=request.POST["selectDate"],
                                               confirmIndicator=1)
    if not bemodel.exists():
        bemodel = models.SelectDate.objects.filter(
            selectDate=request.POST["selectDate"])
        if bemodel.exists():
            bemodel.update(confirmIndicator=1)
            answer = {"requset": "일정확정"}
        else:
            bemodel = models.SelectDate(userId=request.POST.get('user_ID'),
                                        selectDate=request.POST['selectDate'],
                                        dateCount=1,
                                        confirmIndicator=1)
            bemodel.save()
            answer = {"request": "일정좋아요 및 확정"}
    else:
        bemodel.update(confirmIndicator=0)
        answer = {"requset": "확정취소"}
    return JsonResponse(answer)

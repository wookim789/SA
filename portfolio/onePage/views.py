# from django.contrib.auth.models import User
from django.http import JsonResponse
from django.render import render
from . import models
# Create your views here.


def index(request):
    return render(request, 'onePage/index.html')


def getMemberId(request):
    model = models.selectDate.objects.all()
    result = []
    print(request)

    for i in model:
        result.append({"userId": i.userId,
                       "selectDate": i.selectDate,
                       "dateCount": i.dateCount,
                       "confirmIndicator": i.confirmIndicator})
    return JsonResponse(result)


def loadCalendar(request):
    model = models.selectDate.objects.all()
    result = []
    print(request)

    for i in model:
        result.append({"userId": i.userId,
                       "selectDate": i.selectDate,
                       "dateCount": i.dateCount,
                       "confirmIndicator": i.confirmIndicator})
    return JsonResponse(result)

# def selectCalendar(request):
#     selectDate = request.POST["selectDate"]

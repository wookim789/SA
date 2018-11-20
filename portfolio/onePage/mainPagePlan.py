from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.http import HttpResponse
from django.core import serializers


@csrf_exempt
def planListClick(request):
    print(request.POST)
    print(request.POST.get("teamName"))
    print("planListClik")
    if request.POST:
        if "teamName" in request.POST:
            try:
                planModel = serializers.serialize('json',
                                                  models.TemaPlanList.objects.filter(teamName=request.POST.get("teamName")))
                print("return resoponse")
                return JsonResponse(planModel, safe=False)
            except IOError:
                print("db error")
                return JsonResponse({"result": "DBerror"}, safe=False)
        else:
            print("No data")
            return JsonResponse({"result": "NoData"}, safe=False)
    else:
        print("Not Post Access")
        return JsonResponse({"result": "NotPostAcess"}, safe=False)


@csrf_exempt
def planNameAdd(request):
    print("planNameAdd")
    print(request.POST.get("team-name-plan-val"))
    print(request.POST.get("plan-name-val"))
    if request.POST:
        if "plan-name-val" in request.POST:
            try:
                planModel = models.TemaPlanList(
                    teamName=request.POST.get("team-name-plan-val"),
                    teamPlanName=request.POST.get("plan-name-val")
                )
                planModel.save()
                return JsonResponse({"result": True}, safe=False)
            except IOError:
                return JsonResponse({"result": False}, safe=False)
        

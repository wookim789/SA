from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.shortcuts import render
from django.core import serializers
import logging as log

#from django.http import HttpResponse


@csrf_exempt
def planListClick(request):
    #log.debug("planListClick")
    if request.POST:
        if "teamName" in request.POST:
            try:
                planModel = serializers.serialize('json',
                                                  models.TemaPlanList.objects.filter(teamName=request.POST.get("teamName")))
                userAuthority = models.TeamInfo.objects.get(teamName=request.POST.get("teamName"),
                                                            userId=request.POST.get("userId"))

                request.session['leader'] = userAuthority.leader
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
    #log.debug("planNameAdd")
    if request.POST:
        if "planName" in request.POST:
            try:
                planModel = models.TemaPlanList(teamName=request.POST.get(
                    "teamName"), teamPlanName=request.POST.get("planName"))
                planModel.save()
                return JsonResponse({"result": True}, safe=False)
            except IOError:
                print("db error")
                return JsonResponse({"result": False}, safe=False)
        else:
            print("No data")
            return JsonResponse({"result": "NoData"}, safe=False)
    else:
        print("Not Post Access")
        return JsonResponse({"result": False}, safe=False)


@csrf_exempt
def delPlan(request):
    #log.debug("delete Plan")
    if request.POST:
        if "planNo" in request.POST:
            try:
                planNo = request.POST.get("planNo")

                planModel = models.TemaPlanList.objects.filter(
                    teamPlanNo=planNo)
                planModel.delete()

                teamPlan = models.TemaPlanList.objects.filter(
                    teamPlanNo=planNo)
                teamPlan.delete()

                selectDate = models.SelectDate.objects.filter(
                    teamPlanNo=planNo
                )
                selectDate.delete()

                planMap = models.PlanMap.objects.filter(
                    teamPlanNo=planNo
                )
                planMap.delete()
                
                return JsonResponse({"result": True}, safe=False)
            except IOError:
                print("db error")
                return JsonResponse({"result": False}, safe=False)
        else:
            print("No data")
            return JsonResponse({"result": False}, safe=False)
    else:
        print("Not Post Access")
        return JsonResponse({"result": False}, safe=False)

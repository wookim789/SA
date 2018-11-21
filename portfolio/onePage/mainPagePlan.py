from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.shortcuts import render
#from django.http import HttpResponse
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
                userAuthority = models.TeamInfo.objects.get(teamName=request.POST.get("teamName"),
                                                               userId=request.POST.get("userId"))
                print(userAuthority.leader)
                request.session['leader'] = userAuthority.leader

                print("check model json data--------------------")
                #print(planModel)
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
    if request.POST:
        if "planName" in request.POST:
            try:
                planModel = models.TemaPlanList(
                    teamName=request.POST.get("teamName"),
                    teamPlanName=request.POST.get("planName")
                )
                planModel.save()
                return JsonResponse({"result": True}, safe=False)
            except IOError:
                print("plan 저장실패")
                return JsonResponse({"result": False}, safe=False)
    else:
        print("plan 저장실패")
        return JsonResponse({"result": False}, safe=False)


# @csrf_exempt
# def delPlan(request):
#     print("delPlan")
#     if request.POST:
#         if "planNo" in request.POST:
#             try:
#                 planModel = models.TemaPlanList(
#                     planNo=request.POST.get("planNo"))
#                 planListClick.delete()

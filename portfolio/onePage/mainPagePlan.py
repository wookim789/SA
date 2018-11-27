from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models

from django.core import serializers
# import logging as log
# from django.shortcuts import render
# from django.http import HttpResponse



# 페이지 수
def pageNum(x): return int(x / 10) if x % 10 == 0 else int(x/10) + 1

@csrf_exempt
def planListClick(request):

    # log.debug("planListClick")
    if request.POST:
        if "teamName" in request.POST:
            try:
                # 팀네임이 일치하는 플랜 가져오기
                planModelObj = models.TemaPlanList.objects.filter(
                    teamName=request.POST.get("teamName")).order_by('-teamPlanNo')

                # 플랜 게시글 수
                planCountNum = planModelObj.count()

                # 플랜 페이지 수 계산
                planPageNum = pageNum(planCountNum)

                # 플랜 페이지 수 10개씩 계산
                planPageDivNum = pageNum(planPageNum)

                planModelObj = models.TemaPlanList.objects.filter(
                    teamName=request.POST.get("teamName")).order_by('-teamPlanNo')[:10]

                planModel = serializers.serialize('json',
                                                  planModelObj)
                # print(planModelObj)
                # planModel = planModel.update(
                #     )
                userAuthority = models.TeamInfo.objects.get(teamName=request.POST.get("teamName"),
                                                            userId=request.POST.get("userId"))
                # print(planModel)
                del request.session['planPageNum']
                del request.session['planPageDivNum']
                del request.session['leader']
                request.session['planPageNum'] = planPageNum
                request.session['planPageDivNum'] = planPageDivNum
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

    # log.debug("planNameAdd")
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

    # log.debug("delete Plan")
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

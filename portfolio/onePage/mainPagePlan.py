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
def loadPage(request):
    print("load Page")
    if request.POST:
        if ("teamName" in request.POST) and ("pageNum" in request.POST):
            try:
                num = request.POST.get(pageNum)
                startPage = num * 10 - 10
                endPage = num * 10

                planModel = serializers.serialize('json', planModel=TemaPlanList.objects.filter(
                    teamName=request.POST.get("teamName"),).order_by('-teamPlanNo')[startPage:endPage])

                return JsonResponse(planModel, safe=False)
            except IOError:
                print("IO exception")
                return JsonResponse({"result": "IO exception"}, safe=False)
        else:
            print("request no data")
            return JsonResponse({"result": "request no data"}, safe=False)
    else:
        print("not post access")
        return JsonResponse({"result": "not post access"}, safe=False)


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

                # 플랜 내림차순 10개 플랜 가져오기
                planModelObj = models.TemaPlanList.objects.filter(
                    teamName=request.POST.get("teamName")).order_by('-teamPlanNo')[:10]

                # 해당 플랜 객체 json 으로 시리얼 라이즈
                planModel = serializers.serialize('json', planModelObj)

                # 테이블 담은 객체 삭제
                planModelObj = None

                # json 데이터 끝부분 ]자르기
                planModel = planModel.replace("]", "")

                # 팀 선택 시 해당 팀의 권한 정보 조회
                userAuthority = models.TeamInfo.objects.get(teamName=request.POST.get("teamName"),
                                                            userId=request.POST.get("userId"))
                result = ""

                #json 데이터 끝에 페이지 정보 데이터 붙히기
                if planModel == "[":
                    result = '{ "model" : "onePage.teamplanlist",' + \
                        '"pk" : "p", ' + \
                        '"fields" : {' + \
                        '"planPageNum" : "' + str(planPageNum) + \
                        '","planPageDivNum" : "' + str(planPageDivNum) + \
                        '","leader" :"' + \
                        str(userAuthority.leader) + '"}}]'
                else:
                    result = ',{ "model" : "onePage.teamplanlist",' + \
                        '"pk" : "p", ' + \
                        '"fields" : {' + \
                        '"planPageNum" : "' + str(planPageNum) + \
                        '","planPageDivNum" : "' + str(planPageDivNum) + \
                        '","leader" :"' + \
                        str(userAuthority.leader) + '"}}]'
                planModel += result
                print(planModel)
                # 이전의 권한 세션 삭제 및 갱신 -> html 문서의 hidden form 데이터 수정해야함. json 데이터에 붙힘.
                del request.session['leader']
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

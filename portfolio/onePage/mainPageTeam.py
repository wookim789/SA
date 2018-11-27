# from django.contrib.auth.models import User
from django.http import JsonResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.core import serializers


@csrf_exempt
# 유저의 팀 리스트를 보여주기 위함
def loadTeamNameList(request):
    print("access load team list")
    if request.POST:
        if 'userId' in request.POST:
            try:
                # 시리얼 라이즈를 통해 db에서 읽어온 데이터를 바로 json 형태로 변환하여 response객체 전송
                teamListModel = serializers.serialize('json',
                                                      models.TeamInfo.objects.filter(userId=request.POST.get('userId')))
                return JsonResponse(teamListModel, safe=False)
            except IOError:
                print("DB access eror")
                return JsonResponse({"result": False}, safe=False)
    else:
        print("Not Post access. banded access")
        return JsonResponse({"result": False}, safe=False)


@csrf_exempt
def checkTeamName(request):
    if request.POST:
        if 'teamName' in request.POST:
            try:
                # print(request.POST.get("teamName"))
                teamListModel = models.TeamInfo.objects.filter(
                    teamName=request.POST.get('teamName')
                )
                if teamListModel.exists():
                    print("already exists team name")
                    return JsonResponse({'result': False}, safe=False)
                else:
                    print("It's ok")
                    return JsonResponse({'result': True}, safe=False)
            except IOError:
                print("DB access fail")
                return JsonResponse({'result': False}, safe=False)
        else:
            return JsonResponse({'result': False}, safe=False)


@csrf_exempt
def makeTeam(request):
    if request.POST:
        if ('teamName' in request.POST) and ('userId' in request.POST):
            try:

                checkTeamNum = models.TeamInfo.objects.filter(
                    userId=request.POST.get("userId")
                )
                if checkTeamNum.exists() and checkTeamNum.count() < 3:
                    teamModel = models.TeamInfo(
                        teamName=request.POST.get("teamName"),
                        userId=request.POST.get("userId"),
                        leader=1
                    )
                    teamModel.save()
                    return JsonResponse({'result': True}, safe=False)
                return JsonResponse({'result': "teamNumOutOfRange"}, safe=False)
            except IOError:
                print("저장 실패")
                return JsonResponse({'result': False}, safe=False)
    return JsonResponse({"result": False}, safe=False)

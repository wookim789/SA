# from django.contrib.auth.models import User
from django.http import JsonResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models


@csrf_exempt
def loadTeamNameList(request):
    print("access load team list")
    if request.POST:
        if 'userId' in request.POST:
            try:
                teamListModel = models.TeamInfo.objects.filter(
                    userId=request.POST.get('userId')
                )
                if teamListModel.exists():
                    result = []
                    for i in teamListModel:
                        result.append({
                            'teamName': i.teamName,
                        })
                    print("return team name")
                    return JsonResponse(result, safe=False)
                else:
                    print("No have team ")
                    return JsonResponse({"result": "No have Team"}, safe=False)
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
                print(request.POST.get("teamName"))
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
                print(request.POST.get("teamName"))
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
                    print(teamModel)
                    return JsonResponse({'result': True}, safe=False)
                return JsonResponse({'result': "teamNumOutOfRange"}, safe=False)
            except IOError:
                print("저장 실패")
                return JsonResponse({'result': False}, safe=False)
    return JsonResponse({"result": False}, safe=False)

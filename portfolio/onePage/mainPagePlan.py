from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.http import HttpResponse
import django.core.serializers as dcs


@csrf_exempt
def planListClick(request):
    print(request.POST)
    print("planListClik")
    if request.POST:
        if "teamName" in request.POST:
            try:
                planModel = dcs.serialize('json',
                                          [models.TemaPlanList.objects.filter(teamName=request.POST.get("teamName"))])
                # s is a string with [] around it, so strip them off
                o = planModel.strip("[]")

                return HttpResponse(o, mimetype="application/json")

                # for i in planModel.count():
                #      result = {"": }

                # for i in planModel:
                #     result.append({"planNo": i.teamPlanNo,
                #                    "planName": i.teamPlanName})
                # if result == []:
                #     return JsonResponse({"result": "NoResultData"}, safe=False)
                # print("data send")
                # return JsonResponse(result, safe=False)
            except IOError:
                print("db error")
                return JsonResponse({"result": "DBerror"}, safe=False)
        else:
            print("No data")
            return JsonResponse({"result": "NoData"}, safe=False)
    else:
        print("Not Post Acess")
        return JsonResponse({"result": "NotPostAcess"}, safe=False)

# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import models


@csrf_exempt
def checkId(request):
    print("sign view 접근")
    if request.POST:
        # print(try_id)

        try_id = request.POST.get("sign-id-val")
        signModel = models.UserCount.objects.filter(userId=try_id)

        if signModel.exists():
            # print("id already exist")
            return JsonResponse({"result": False}, safe=False)

    return JsonResponse({"result": True}, safe=False)


@csrf_exempt
def signUp(request):
    print("signup 접근")
    try:
        print(request.POST.get('sign-id-val'))
        signModel = models.UserCount(userId=request.POST.get('sign-id-val'),
                                     userPw=request.POST.get('sign-pw-val'),
                                     email=request.POST.get('sigh-email-val'),
                                     teamCount=0)

        signModel.save()
        print(signModel)
        return JsonResponse({"result": True}, safe=False)
    except IOError:
        print("저장 실패")
        return JsonResponse({"result": False}, safe=False)


# userId userPw email teamCount
#     signModel = models.UserCount(userId=request.POST.get('user_ID'),
#                                   selectDate=request.POST['selectDate'],
#                                   dateCount=cnt,
#                                   confirmIndicator=0)
#         model.save()
#         bemodel.update(dateCount=cnt)

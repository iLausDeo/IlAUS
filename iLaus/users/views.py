# from django.shortcuts import render

# Create your views here.
import json

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import UserInfo
from iLaus.constant import const

def login_handler(req):
    if req.method == "POST":
        print(post)
        return_json = {"status": const.SUCCESS_STATUS}
        return HttpResponse(json.dumps(return_json))
    return_json = {"status": const.SUCCESS_STATUS}
    return HttpResponse(json.dumps(return_json))





    # if req.method == "GET":
    #     return render(req, "user/msite/login.html", {"redirect": redirect_view_req})
    # elif req.method == "POST":
    #     tel = req.POST.get("Tel", None)
    #     password = req.POST.get("Passwd")
    #     if not tel or not password:
    #         return HttpResponse(json.dumps({"code": 6104}))
    #     url = '/api/login/passwdlogin/'
    #     uri = LOGIN_SERVICE_PREFIX + url
    #     data = {'Tel': tel,
    #             'Passwd': password
    #             }
    #     return_json = requestS.request("POST", uri, data=data)
    #     if return_json["code"] == 6200:
    #         user_info_list = UserInfo.objects.filter(tel=tel)
    #         if not user_info_list:
    #             return HttpResponse(json.dumps({"code": 6104}))
    #         user_info = user_info_list.first()
    #         req.session['user_id'] = user_info.user_id
    #         redirect_view = re.compile("aaa00aaa").sub("&", redirect_view_req)
    #         l = HttpResponse(json.dumps({"code": 200, "redirect_view": redirect_view}))
    #         l.set_cookie("user_id", user_info.user_id)
    #         if user_info.openid:
    #             req.session["openid"] = user_info.openid
    #             l.set_cookie("openid", user_info.openid)
    #         req.session['bind'] = user_info.status
    #         l.set_cookie("bind", user_info.status)
    #         return l
    #     return HttpResponse(json.dumps(return_json))
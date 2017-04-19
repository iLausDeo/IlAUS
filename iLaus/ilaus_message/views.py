import json
import hmac
import uuid
import random
import string
import base64
import hashlib
import requests
import urllib.parse

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from iLaus.constant import const



# Create your views here.

def sms_handler(req):
    parameter = get_Signature(sign_name="ilaus网络", template_code="SMS_61795035",
        rec_num="13917990164", param_string='{"name":"王浩原","auth_code":"'+str(random.randint(100000,999999))+'"}')
    serialized_parameter = get_serialized_str(parameter)
    sign_code = aliyun_sign(settings.ALIYUN_ACCESS_KEY_SECRET, serialized_parameter)
    Signature = get_urlparse_encode(sign_code)
    # return get_serialized_str(parameter)

    # tel = req.POST.get("tel", None)
    # if not tel:
    #     return HttpResponse(json.dumps({'status':const.NOTFOUND_FIELD_STATUS, 'msg':'没有发现电话号码！'}))
    # random.randint(100000,999999)
    return HttpResponse(json.dumps({'status':const.SUCCESS_STATUS, 'msg':'短信发送成功，请前往信息处查看！'}))

def test_a():
    parameter = {"AccessKeyId":'testid',
    "Action":'SingleSendSms',
    "Format":'XML',
    "ParamString":'{"name":"d","name1":"d"}',
    "RecNum":'13098765432',
    "RegionId":'cn-hangzhou',
    "SignName":'标签测试',
    "SignatureMethod":'HMAC-SHA1',
    "SignatureNonce":'9e030f6b-03a2-40f0-a6ba-157d44532fd0',
    "SignatureVersion":'1.0',
    "TemplateCode":'SMS_1650053',
    "Timestamp":'2017-04-19T23:05:52Z',
    "Version":'2016-09-27'}

    serialized_parameter = get_serialized_str(parameter)
    sign_code = aliyun_sign("testsecret", serialized_parameter)
    Signature = get_urlparse_encode(sign_code)
    print(Signature)
    parameter["Signature"] = Signature

    url = "http://sms.aliyuncs.com/"
    print(parameter)
    # kwargs['params'] = parameter
    headers={'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, data=parameter,  headers=headers)
    print(r.text)
    return True

def test():

    parameter = get_Signature(sign_name="ilaus网络", template_code="SMS_61795035",
        rec_num="13917990164", param_string='{"name":"king","auth_code":"'+str(random.randint(100000,999999))+'"}')
    print(parameter)
    serialized_parameter = get_serialized_str(parameter)
    sign_code = aliyun_sign(settings.ALIYUN_ACCESS_KEY_SECRET, serialized_parameter)
    Signature = get_urlparse_encode(sign_code)
    print(Signature)
    parameter["Signature"] = Signature

    url = "http://sms.aliyuncs.com/"
    print(parameter)
    # kwargs['params'] = parameter
    headers={'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, data=parameter,  headers=headers)
    print(r.text)
    # r = requests.request(
    #     method=method,
    #     url=url,
    #     verify=False,
    #     **kwargs
    # )
    # r.raise_for_status()
    return True

def get_urlparse_encode(wait_code):
    return urllib.parse.urlencode({"key": wait_code}).split("=",1)[1]

def aliyun_sign(secret, encode_str):
    # hmac
    key = bytes(secret+"&", 'UTF-8')
    message = bytes(encode_str, 'UTF-8')
    digester = hmac.new(key, msg=message, digestmod=hashlib.sha1)
    signature1 = digester.digest()
    # sha1
    signature2 = base64.b64encode(signature1)
    return str(signature2, "UTF-8")

def get_Signature(**kwargs):
    parameter = {
        "Format":"JSON",
        "Version":"2016-09-27",
        "AccessKeyId": settings.ALIYUN_ACCESS_KEY_ID,
        "SignatureMethod":"HMAC-SHA1",
        "Timestamp": get_utc_now(),
        "SignatureVersion":"1.0",
        "SignatureNonce":get_uuid_str(),
        "RegionId": settings.ALIYUN_SMS_REGIONID,
        "Action":"SingleSendSms",
        "SignName": kwargs.get("sign_name"),
        # "ilaus网络",
        "TemplateCode": kwargs.get("template_code"),
        # "SMS_61795035",
        "RecNum": kwargs.get("rec_num"),
        # "13917990164",
        "ParamString": kwargs.get("param_string")
        # '{"name":"王浩原","auth_code":"'+str(random.randint(100000,999999))+'"}'
    }
    return parameter
    # print(get_serialized_str(parameter))
    # return get_serialized_str(parameter)


def get_serialized_str(dict_val):
    # import pdb; pdb.set_trace()
    param_items = list(dict_val.items())

    param_items.sort()
    # print(param_items)

    _n_param = []
    for key, val in param_items:
        key = urllib.parse.urlencode({"k": key}).split("=", 1)[1]
        val = urllib.parse.urlencode({"k": val}).split("=", 1)[1]
        _n_param.append([key, val])
    # urlencode
    _str = ["%s=%s" % (key, val) for key, val in _n_param]
    _encode_str = "&".join(_str)
    # print(_encode_str)

    # url / parse
    _parse = urllib.parse.urlencode({"k": "/"}).split("=", 1)[1]
    _encode_str = urllib.parse.urlencode({"key": _encode_str}).split("=", 1)[1]
    # 加入GET&/&
    encode_str = "POST&" + _parse + "&" + _encode_str
    print(encode_str)
    return encode_str


    # return_str = ""
    # key_list = sorted(dict_val.keys(), key=lambda item:item[0])
    # for key in key_list:
    #     return_str += key + "=" + dict_val[key] + "&"
    # return return_str[:-1]


def get_utc_now():
    """
    当前utc时间
    """
    _format = "%Y-%m-%dT%H:%M:%SZ"
    _now = datetime.utcnow()
    return _now.strftime(_format)


def get_random_num(data=None):
    """
    得到随机字符串
    """
    if not data:
        data = string.ascii_letters
    nonce_list = [random.choice(data) for x in range(14)]
    nonce = "".join(nonce_list)
    return nonce

def get_uuid_str():
    return str(uuid.uuid1())
# 排序
# dict_val = {"a":"asd", "b":"asd"}
# sorted(dict_val.keys(), key=lambda item:item[0])





import ssl
# ssl._create_default_https_content = ssl.create_unverified_content // ssl 认证

from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from django.conf import settings

def send_sms_single(phone_num, template_id, param_list):
    """
    :param phone_num: 手机号
    :param template_id: 短信模版id
    :param param_list: 短信模板所需参数
    :return:
    """

    appid = settings.TENCENT_SMS_APP_ID
    appkey = settings.TENCENT_SMS_APP_KEY
    sms_sign = settings.TENCENT_SMS_SIGN
    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': '网络异常，短信发送失败'}
    return response


def send_sms_multi(phone_num_list, template_id, param_list):
    """
    :param phone_num_list: 手机号列表
    :param template_id: 短信模版id
    :param param_list: 短信模板所需参数
    :return:
    """

    appid = settings.TENCENT_SMS_APP_ID
    appkey = settings.TENCENT_SMS_APP_KEY
    sms_sign = settings.TENCENT_SMS_SIGN
    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': '网络异常，短信发送失败'}
    return response

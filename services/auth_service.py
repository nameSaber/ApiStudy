from core.result_base import ResultBase, pre_assertion
from pages.auth_page import auth
from testcases.conftest import login_authorization


def get_auth_login(username, password):
    """登录用户"""
    result = ResultBase()
    result.success = False
    payload = {
        "username": username,
        "password": password
    }
    headers = {
        "Authorization": ""
    }
    resp = auth.login(data=payload, headers=headers)
    pre_assertion(resp, result)
    return result


def get_auth_cpatcha():
    """获取登录验证码"""
    result = ResultBase()
    result.success = False
    headers = {
        'Authorization': ''
    }
    resp = auth.captcha(headers=headers)
    pre_assertion(resp, result)
    return result


def get_auth_logout(login_info):
    """用户注销"""
    result = ResultBase()
    result.success = False
    Authorization = login_authorization(login_info)
    headers = {
        'Authorization': Authorization
    }
    resp = auth.logout(headers=headers)
    pre_assertion(resp, result)
    return result

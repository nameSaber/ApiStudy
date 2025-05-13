import pytest
import allure
from services.auth_service import *
from testcases.conftest import auth_data
from core.result_base import *


@allure.step("步骤 ==>> 登录用户")
def step_login(username):
    logger.info("步骤 ==>> 登录用户：{}".format(username))

@allure.step("步骤 ==>> 获取登录验证码")
def step_captcha():
    logger.info("步骤 ==>> 获取登录验证码")

@allure.step("步骤 ==>> 用户注销登录")
def step_logout():
    logger.info("步骤 ==>> 用户注销登录")


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("认证中心模块")
class TestAuth:

    @allure.story("用例--登录用户成功")
    @allure.description("该用例是针对获取用户登录成功情况的测试")
    @allure.title("测试数据：【 {username}，{password}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             auth_data["test_auth_login_success"])
    def test_auth_login_success(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_auth_login(username, password)
        step_login(username)
        assert_success(result, except_result, except_code, except_msg)
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--登录用户失败")
    @allure.description("该用例是针对获取用户登录失败情况的测试")
    @allure.title("测试数据：【 {username}，{password}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             auth_data["test_auth_login_failure"])
    def test_auth_login_failure(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_auth_login(username, password)
        step_login(username)
        assert_failure(result, except_result, except_code, except_msg)
        logger.info("*************** 结束执行用例 ***************")


    @allure.story("用例--获取登录验证码")
    @allure.description("该用例是针对获取登录验证码情况的测试")
    @allure.title("测试数据：【 {except_result}，{except_code}，{except_msg}】")
    @pytest.mark.parametrize("except_result, except_code, except_msg",
                             auth_data["test_auth_captcha"])
    def test_auth_captcha(self, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_auth_cpatcha()
        step_captcha()
        assert_success(result, except_result, except_code, except_msg)
        logger.info("*************** 结束执行用例 ***************")


    @allure.story("用例--用户注销登录")
    @allure.description("该用例是针对获取用户注销登录情况的测试")
    @allure.title("测试数据：【 {except_result}，{except_code}，{except_msg}】")
    @pytest.mark.parametrize("except_result, except_code, except_msg",
                             auth_data["test_auth_logout"])
    def test_auth_logout(self, login_fixture, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_auth_logout(login_fixture)
        step_logout()
        assert_success(result, except_result, except_code, except_msg)
        logger.info("*************** 结束执行用例 ***************")






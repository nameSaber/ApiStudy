import pytest
import os
import allure
from pages.auth_page import auth
from utils.read_data import data
from utils.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data

base_data = get_data("base_data.yml")
auth_data = get_data("auth_data.yml")

@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, msg):
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, msg))



@pytest.fixture(scope="session")
def login_fixture():
    """用户登录前置"""
    username = base_data["init_admin_user"]["username"]
    password = base_data["init_admin_user"]["password"]
    header = {
        "Authorization": ""
    }
    payload = {
        "username": username,
        "password": password
    }
    login_info = auth.login(data=payload, headers=header)
    step_login(username, login_info.json()["msg"])
    yield login_info.json()


def login_authorization(login_fixture):
    """获取登录Authorization"""
    user_info = login_fixture
    token_type = user_info["data"]["tokenType"]
    accessToken = user_info["data"]["accessToken"]
    Authorization = token_type + " " + accessToken
    return Authorization

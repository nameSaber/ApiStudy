import os

from core.req_client import ReqClient
from utils.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "utils", "setting.ini")
test_url = data.load_ini(data_file_path)["ENV"]["test_url"]


class Auth(ReqClient):
    def __init__(self, test_url, **kwargs):
        super().__init__(test_url, **kwargs)

    # 用户登录
    def login(self, **kwargs):
        return self.post("/auth/login", **kwargs)

    # 登录验证码
    def captcha(self, **kwargs):
        return self.get("/auth/captcha", **kwargs)

    # 用户注销登录
    def logout(self, **kwargs):
        return self.delete("/auth/logout", **kwargs)


auth = Auth(test_url)

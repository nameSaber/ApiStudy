from utils.logger import logger


class ResultBase:
    """响应结果"""
    def __init__(self):
        self.success = False  # 操作是否成功
        self.error = None  # 错误信息
        self.msg = ""  # 消息文本
        self._raw_response = None  # 原始响应对象
        self._status_code = None  # 独立存储状态码
        self._json_data = {}  # 解析后的JSON数据

    @property
    def response(self):
        """返回响应对象（实际值或代理对象）"""
        return self._raw_response if self._raw_response is not None else self._NullResponse()

    @response.setter
    def response(self, value):
        """设置响应对象时自动提取关键数据"""
        self._raw_response = value
        self._status_code = getattr(value, 'status_code', None)

        # 安全解析JSON
        try:
            self._json_data = value.json() if value else {}
        except (ValueError, AttributeError):
            self._json_data = {}

    @property
    def status_code(self):
        """获取状态码（优先返回真实值）"""
        return self._status_code if self._status_code is not None else 0

    def json(self):
        """兼容 response.json() 的调用方式"""
        return self._json_data

    class _NullResponse:
        """内部使用的空响应代理"""

        @property
        def status_code(self):
            return 0

        def json(self):
            return {}


"""
响应结果预判断
"""
def pre_assertion(response, result):
    if response.json()["code"] == "00000":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(response.json()["code"], response.json()["msg"])
    result.msg = response.json()["msg"]
    result.response = response
    logger.info("用户注销登录 ==>>  返回结果 ==>> {}".format(result.response.text))


"""
assert模版
"""
def assert_success(result, except_result, except_code, except_msg):
    assert result.success == except_result, result.error
    assert result.response.status_code == 200
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
    assert result.response.json().get("code") == except_code
    assert except_msg in result.msg

def assert_failure(result, except_result, except_code, except_msg):
    assert result.success == except_result, result.error
    assert result.response.status_code == 400
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
    assert result.response.json().get("code") == except_code
    assert except_msg in result.msg

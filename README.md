## 本项目是对于 https://vue.youlai.tech/#/dashboard 的接口文档所制作的，用于个人学习用途。

## 技术栈 ： python + pytest + request + pymsql + yaml + allure

## allure 测试报告
### 执行命令
```python
# pytest -vs --alluredir ./OutPuts/report/result --clean-alluredir # 生成原始文件，不能打开html报告

# allure serve ./OutPuts/report/allure-report # 打开html的报告需要启动allure服务

# --clean  # --clean 清除上一次的测试报告
# allure generate ./OutPuts/report/result -o ./OutPuts/report/allure-report -c


# allure open ./OutPuts/report/allure-report --host 192.168.0.104 --port 8800  # 打开报告
```

## 本项目参考https://github.com/wintests/pytestDemo

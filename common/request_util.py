import requests
import json
from common.loggin_util import LoggingUtil


# requests的简单封装
class RequestUtil:
    # 设置单例模式
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, "_instance"):
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self, env: str = 'test_env', init_token=False, **kwargs):
        self.session = requests.sessions.Session()
        # 这是命令行传参，决定当前是否正式/测试环境的参数
        self.kwargs = kwargs
        # 初始化日志系统
        logging_util_temp = LoggingUtil(__name__)
        self.logging_util = logging_util_temp.init_logger()

    def request_util(self, data: dict):

        # data是个测试用例，以下代码是根据测试用例进行的接口请求
        if data["method"].upper() == "GET":
            if data["params"] is not None:
                url = data["api"] + "?" + data["params"]

            else:
                url = data["api"]
            self.logging_util.info(url)

            responses = self.session.request(method=data["method"], url=url, **self.kwargs)
        elif data["method"].upper() == "POST":
            if data["json_data"] is not None:
                url = data["api"]
                json_data = json.loads(data["json_data"])
                params_data = data["params"]

                self.logging_util.info(url)
                self.logging_util.info(data["json_data"])
                self.logging_util.info(data["params"])

                responses = self.session.request(method=data["method"], url=url, json=json_data, params=params_data, **self.kwargs)
            elif data["x_www_form_urlencoded_data"] is not None:
                url = data["api"]
                data_data = json.loads(data["x_www_form_urlencoded_data"])
                params_data = data["params"]

                self.logging_util.info(url)
                self.logging_util.info(data["x_www_form_urlencoded_data"])
                self.logging_util.info(data["params"])

                responses = self.session.request(method=data["method"], url=url, data=data_data, params=params_data, **self.kwargs)
            else:
                raise requests.exceptions.RequestException("不支持的传参类型")
        else:
            raise requests.exceptions.RequestException("不支持的请求方法")

        return responses

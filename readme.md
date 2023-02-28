A.简要介绍
    1.该项目应用于第三方接口测试（不需要token信息的接口）
    2.运行项目后，可以对 testcase_data/excel/testcase_api.xlsx文件 中记录的接口进行简单的连通性测试（只测试该调用接口是否响应码为200）
    3.运行完成后将：
        生成运行日志.log
        钉钉通知对应调用的钉钉机器人，报告接口测试集中是否有调用失败的接口
        生成一份测试报告

B.使用方法
    1.安装Python 
    2.安装pip 工具
    3.更换pip源
    4.再根目录下打开cmd，输入pip install -r requirements.txt。初始化项目环境
    5.在testcase_data/excel/testcase_api.xlsx 中编写接口相关测试数据
    6.在cmd界面中输入run_test.py 或者 python run_test.py 运行项目
    

C.*要点须知
    1.只能进行不需要令牌验证的接口测试

    2.testcase_data/excel/testcase_*.xlsx 中testcase_data存放将要进行接口测试的相关数据
        name: 自定义接口名
        method:该接口请求方法
        api: 接口全部url
        params:一般是get请求的入参，有则输入，无则置空
        json_data:一般是post请求的入参，当入参为json字符串时输入
        x_www_form_urlencoded_data：一般是post请求的入参，当入参为表单数据时输入

    3.config/config_file.py 中可以对钉钉机器人相关信息进行定义

    4.pytest.ini 文件可以对pytest框架命令行相关信息进行定义
        --html:生成测试报告 html格式
        --reruns * --reruns-delay *：失败重跑定义
        -n ：多线程执行定义

    5.loggin文件夹下存放运行日志相关信息
    6.report存放接口测试报告
    7.不要进行包含动态参数的接口测试
    
        
    
D.额外事项
    1.建议集成jenkins 建立接口自动化测试项目
    2.建议扩展allure插件，生成美观的测试报告
    3.钉钉机器人只能调用 加签类型，且通知文案采用预置

    
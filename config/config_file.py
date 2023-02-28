# 钉钉机器人相关配置

# 钉钉机器人webhook：webhook + access_token
dd_robot_webhook = r"https://oapi.dingtalk.com/robot/send"
dd_robot_access_token = {"access_token": "cb8b4075e157bacc79d57fb1a7287dc7c4db76a92f14f93a15df95af02bb602c"}

# 调用钉钉机器人headers定义
dd_robot_headers = {'Content-Type': 'application/json'}

# 钉钉机器人加签数据定义
dd_secret = 'SECf9a03351a85d667ae734d7f17cc7bed61ac0ce63452d739142420624e993ec56'



# testcase_excel格式定义，不能更改
xlsx_format = ("name", "method", "api", "params", "json_data", "x_www_form_urlencoded_data")


# coding:utf-8
import os

# Application的参数
settings = {
    'static_path': os.path.join(os.path.join(__file__), 'static'),
    'debug': True,
    'cookie_secret': 'dd7NZLYwRQ2ziRa2krLYr07MqWZ+s0HYjkBtAFnAAeQ=',
    # 'xsrf_cookies': 'LMlKmzSTR02uct28j9dR+wQBzP5US0llriJpN0FYs2E='
}

# mysql的配置参数
mysql_options = dict(
    host="47.99.192.17",
    port=3306,
    db="ihome",
    user="root",
    passwd="ihome_123456",
    charset="utf8",
)

# redis的配置参数
redis_options = dict(
    host="47.99.192.17",
    port="6379"
)

# log日志的文件路径
log_file = os.path.join(os.path.dirname(__file__), 'logs/log')
log_level = 'warning'

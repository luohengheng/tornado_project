# coding:utf-8

from tornado.web import RequestHandler
import json
from utils.session import SessionHandler
"""
hander基类
"""

class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.redis

    def initialize(self):
        pass

    def prepare(self):
        # 处理发送过来的数据是json
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.json_arg = json.loads(self.request.body)
        else:
            self.json_arg = None

    def set_default_headers(self):
        # 默认返回的数据都是json串
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    def write_error(self, status_code, **kwargs):
        pass

    def on_finish(self):
        pass

    def get_current_user(self):
        session = SessionHandler(self)
        return session.data
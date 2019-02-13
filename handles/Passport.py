# coding: utf-8
from .BaseHandler import BaseHandler
import logging
from utils.response_code import RET, error_map
from utils.session import SessionHandler


class IndexHandler(BaseHandler):
    def get(self):
        # self.db
        # self.redis
        # logging.debug("debug msg")
        logging.warning("warning msg")
        print('print msg')
        self.write('index')


class LoginHandler(BaseHandler):
    """
    登录
    """

    # @tornado.web.authenticated
    def post(self):
        user = self.get_argument('user')
        pwd = self.get_argument('pwd')


        # try:
        # 加入user = lwh pwd = 123 登录成功
        if user == 'lwh222' and pwd == '1222':
            session = SessionHandler(self)
            # session.clear()
            session.data = dict(user=user, pwd=pwd)
            session.save()
            self.write(dict(errno=RET.OK, err_msg=error_map.get(RET.OK)))
        else:
            self.write(dict(errno='', err_msg='账号或者密码有误'))
        # except Exception as e:
        #     logging.error(e)
            self.write({'errno': RET.LOGINERR, 'err_msg': error_map.get(RET.LOGINERR)})


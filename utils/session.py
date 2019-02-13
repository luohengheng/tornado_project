# coding:utf-8
import uuid
import logging
import json
from constants import SESSION_EXPIRES_SECONDS

class SessionHandler(object):
    """
    创建session
    """
    def __init__(self, request_header):
        self.request_header = request_header
        self.session_id = self.request_header.get_secure_cookie('session_id')
        if not self.session_id:
            # self.session_id = str(uuid.uuid4())
            self.session_id = '11'
            self.data = {}
        else:
            try:
                data = self.request_header.redis.get('sess_new_%s' % self.session_id.decode('utf-8'))
            except Exception as e:
                logging.error(e)
                self.data = {}

            if not data:
                self.data = {}
            else:
                self.data = json.loads(data)

    def save(self):
        # try ....except...else 语句，当没有异常发生时，else中的语句将会被执行。
        try:
            json_data = json.dumps(self.data)
            self.request_header.redis.setex('sess_new_%s' % self.session_id,
                                            SESSION_EXPIRES_SECONDS, json_data)
        except Exception as e:
            raise Exception("session save failed")
            logging.error(e)
        else:
            self.request_header.set_secure_cookie('session_id',
                                                  self.session_id)

    def clear(self):
        try:
            self.request_header.redis.delete('sess_new_%s' % self.session_id)
        except Exception as e:
            logging.error(e)


# coding:utf-8
from handles.BaseHandler import BaseHandler
from utils.commons import request_login
import os

class ProfileHandler(BaseHandler):

    @request_login
    def get(self):
        self.write("个人信息")


class UploadFileHandler(BaseHandler):
    """
    文件上传
    """
    def post(self):
        files_url = list()
        pre_url = 'http://192.168.9.190:8000/images/'

        for item in self.request.files.get('house_img'):
            base_path = os.path.dirname(os.path.dirname(__file__))
            images_path = os.path.join(base_path, 'html/images/')
            img_file = open('%s%s' % (images_path, item.filename), 'wb')
            img_file.write(item['body'])
            img_file.close()
            print('%s 保存成功' % item.filename)
            files_url.append(os.path.join(pre_url, item.filename))

        self.write(dict(files_url=files_url))
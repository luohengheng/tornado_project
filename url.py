# coding:utf-8
from handles import Passport, VerifyCode, Profile
from tornado.web import StaticFileHandler
import os

handlers = [
    # (r'/', Passport.IndexHandler),
    (r'/api/imagecode', VerifyCode.ImageCodeHandler),
    (r'/api/telcode', VerifyCode.SmsCode),
    (r'/api/login', Passport.LoginHandler),
    (r'/api/userinfo', Profile.ProfileHandler),
    (r'/api/upload_files', Profile.UploadFileHandler),
    (r'/(.*)', StaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "html"),
                                       default_filename='index.html'))
]
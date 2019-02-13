# coding:utf-8
from .BaseHandler import BaseHandler
from utils.captcha.captcha import captcha
import logging
import constants
from utils.yuntongxun.CreateSingle import SingleHandler
from utils.response_code import RET, error_map
from utils.session import SessionHandler

class ImageCodeHandler(BaseHandler):
    """
    获取图片验证码
    """
    def get(self):
        code_id = self.get_argument('codeid')
        pre_code_id = self.get_argument('pcodeid')
        if pre_code_id:
            try:
                # 图片刷新需要将redis中之前的图片删除
                self.redis.delete("image_code_%s" % pre_code_id)
            except Exception as e:
                logging.error(e)

        # name 获取生成验证码的名字
        # text 获取生成验证码的文本
        # image 获取生成验证码的二进制
        name, text, image = captcha.generate_captcha()
        try:
            self.redis.setex("image_code_%s" % code_id,
                             constants.IMAGE_CODE_EXPIRES_SECONDS, text)
        except Exception as e:
            logging.error(e)
            self.write("")
        self.set_header('Content-Type', 'image/jpg')
        self.write(image)


class SmsCode(BaseHandler):
    """
    获取短信验证码
    todo all(迭代器) 如果迭代器中的值都是真，返回true 迭代器为空 也返回true
    """
    def post(self):
        tel = self.json_arg.get('tel')
        codeid = self.json_arg.get('codeid')

        if not all((tel, codeid, )):
           return self.write({'errno': '', 'err_msg': '参数不全'})

        red_val = self.redis.get("image_code_%s" % 123)
        print(red_val)
        if not self.redis.get("image_code_%s" % 123):
            return self.write({'errno': '', 'err_msg': '图形验证码失效'})

        if red_val.decode('utf-8') != codeid:
            return self.write({'errno': '', 'err_msg': '验证码不一致'})

        try:
            sms_obj = SingleHandler.instance()
            # 模拟获取短信验证码
            sms_obj.send_sms()
            self.write({'errcode': RET.OK, 'err_msg': error_map.get(RET.OK)})
        except Exception as e:
            logging.error(e)
            self.write({'errcode': RET.THIRDERR, 'err_msg': error_map.get(RET.THIRDERR)})


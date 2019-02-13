# coding:utf-8

"""
云通讯现在只是支持Python2不支持3，所以下面只是实现下单利模式
"""


class SingleHandler(object):
    def __init__(self):
        print("初始化")

    @staticmethod
    def instance():
        """
        将单利对象设置成类属性，同时根据判断是否_instance属性是否存在，存在直接返回，不存在创建
        :return:
        """
        if not hasattr(SingleHandler, 'single_instance'):
            SingleHandler.single_instance = SingleHandler()
        return SingleHandler.single_instance

    def send_sms(self):
        print('第三方发送验证码成功')



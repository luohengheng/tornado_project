# coding:utf-8

from tornado import web, httpserver, options, ioloop
from url import handlers
from config import settings
import pymysql
import redis
import config


options.define('port', default=8000, type=int, help='端口')


class MyApplication(web.Application):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.db = pymysql.connect(
            **config.mysql_options
        )
        self.redis = redis.StrictRedis(
            **config.redis_options
        )


def main():
    options.log_file_prefix = config.log_file
    options.logging = config.log_level
    options.parse_command_line()
    app = MyApplication(
        handlers, **settings
    )

    server = httpserver.HTTPServer(app)
    server.listen(options.options.port)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
import os
from flask_script import Manager,Server
from blog import blog

manager = Manager(blog)
manager.add_command('runserver',
                    Server(host='127.0.0.1', port=8000, use_debugger=True))


if __name__ == '__main__':
    manager.run()
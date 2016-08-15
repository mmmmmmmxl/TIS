# Thinking in the study #
#这其实就是个坑#
===============================================

- `permutation.py`：排列组合分组实现

- `wxhongbao.py`：微信红包算法Python实现

- `interview.py`: 一道有趣的面试题（有未解决的疑惑）

- `send_post.py`: POST接口测试工具


===============================================
- `Django_login.py`:

用户的身份验证过程：
1. 首先通过 authenticate() 方法对传入的用户名、密码等信息进行验证，如果符合，则返回相应的 user 对象，同时，该方法会对 user 对象加以标注，通过附加 user.backend 属性来记录验证是被哪个配置的 backend 通过的。默认只有一个 backend，是 django.contrib.auth.backends.ModelBackend.
2. login 方法调用
    如果上一步身份验证通过，则此方法中对 request.session 中简单的添加两个键值：
    (1) "_auth_user_id"  这个是 user.id
    (2) "_auth_user_backend" 这个是 user.backend
因此只要给DJango一个user对象和user.id,user.backend就可以实现任意用户不用密码改变登录态



====================================================
#关于密码传输的一些思考#

写登录页面的时候偶然想到密码通过POST传输的时候是明文传输，只需要抓包即可看到用户的信息。

想过JS加密，然后服务端解密，实际上可行性不高。

知乎上有具体的解决办法，但是似乎除了Https外没有其他可靠的办法。

https://www.zhihu.com/question/20060155


=====================================================
#关于使用JavaScript发送POST请求的跨域问题#
现有的JQuery Ajax发送POST请求无法跨域完成
在net上找了好久好久，好像都没一个完美的解决方案
总结一下net上现有这几种方法：
1.直接用jquery中$.getJSON进行跨域提交
          优点：有返回值,可直接跨域；
          缺点：数据量小；
          提交方式：仅get (无$.postJSON)

2.在页面中嵌入一个iframe，把iframe的宽和高设置为0进行跨域提交
           优点：可直接跨域；
           缺点：无返回值(脱离ajax本质)；
          提交方式：get/post

3.直接用$.post跨域，先提交到本地域名下一个代理程序，通过代理程序向目的域名进行post或get提交，并根据目的域名的返回值通过代理 程序返回给本地页面
          优点：有返回值，可直接跨域，可通过 代理程序 统计ip等用户信息，增加安全性；
          提交方式：get/post
          复杂度：需要前端工程师和后端工程师配合(php/java../工程师)  
           缺点：需要消耗本地服务器资源，增加ajax等待时间（可忽略）

4.通过配置对方nginx的方式来实现跨域的可能（对方愿意配合的情况下）[采用的解决方法]
在location中加入这行add_header Access-Control-Allow-Origin "*";
其中*代表所有域名皆可跨域传输，出于安全考虑，建议将*换为需要跨域传输的域名。


=======================================================
#Django的拾遗之Signal#
使用Signal之前得明白django signal和异步消息列队(例如celery)的区别. signal是同步处理, 因此通过signal调用大处理量的进程时并不能提高性能. 事实上, 将这些需要大处理量的进程移到signal中被视作是一种不好的习惯.
```python
from django.dispatch import Signal 

#定义一个person信号，它产生了"weight"和"height"两个参数的接收器
person = Signal(providing_args = ['weight','height'])

#发送信号有两种方法,Signal.send和Siganal.send_robust，通常我们使用Signal.send
#他们俩的区别在于send不会捕捉异常，而send_robust会捕捉异常
class Person_manage(object):
	...
	def send_person(self,weight,height):
		#send返回的是一个tuple列表,在绝大多数的时候，sender后面是一个类。		
		person.send(sender=self.__class__, height=height, weight=weight)
		
#定义一个方法接收Signal
def my_callback(sender, **kwargs):
   print("Signal received!")

#连接到Signal的两种方法
1.from django.core.signals import request_finished
  request_finished.connect(my_callback)

2.from django.core.signals import request_finished
  from django.dispatch import receiver

  @receiver(request_finished)
  def my_callback(sender, **kwargs):
      print("Request finished!")

#只接收指定信号的方法
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel


@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs):
    ...

```


=======================================
#Python冒泡排序的实现（有sort在似乎根本没什么必要？）#
````python
array = [1,3,5,4,2]
for i in range(len(array))[::-1]:
    for j in range(i):
	if array[j] > array[j+1]:
	    array[j],array[j+1] = array[j+1],array[j]
```


==========================================
#Django中扩展manage.py命令

我们都用过Django的django-admin.py和manage.py。django-admin.py是一个命令行工具，可以执行一些管理任务，比如创建Django项目。而manage.py是在创建每个Django project时自动添加在项目目录下的，只是对manage.py的一个简单包装，其功能是将Django project放到sys.path目录中，同时设置DJANGO_SETTINGS_MODULE环境变量为当前project的setting.py文件。

django-admin.py调用django.core.management来执行命令:
```python
#!/usr/bin/env python
from django.core import management
  
if __name__ == "__main__":
  management.execute_from_command_line()
```

excute_from_command_line()函数会根据命令行参数解析出命令的名称，根据命令名称调用相应的Command执行命令。Command位于各个管理模块的commands模块下面。
所谓管理模块，是指在app模块下的名字为management的模块。Django通过django.core.management.find_management_module函数发现"管理模块":

```python
django.core.management.find_management_module()
def find_management_module(app_name):
  """
  Determines the path to the management module for the given app_name,
  without actually importing the application or the management module.

  Raises ImportError if the management module cannot be found for any reason.
  """
  parts = app_name.split('.')
  parts.append('management')
  parts.reverse()
  part = parts.pop()
  path = None
```

然后通过django.core.management.find_commands函数找到命令类。find_commands函数会在管理模块下查找.py文件，并将.py文件的名称匹配到命令名称:

```python
def find_commands(management_dir):
  """
  Given a path to a management directory, returns a list of all the command
  names that are available.

  Returns an empty list if no commands are defined.
  """
  command_dir = os.path.join(management_dir, 'commands')
  try:
    return [f[:-3] for f in os.listdir(command_dir)
      if not f.startswith('_') and f.endswith('.py')]
  except OSError:
  return []
```

最后，通过django.core.management.load_command_class函数加载该.py文件中的Command类:

```python
def load_command_class(app_name, name):
  """
  Given a command name and an application name, returns the Command
  class instance. All errors raised by the import process
  (ImportError, AttributeError) are allowed to propagate.
  """
  module = import_module('%s.management.commands.%s' % (app_name, name))
  return module.Command()
```

在执行命令的时候，会执行相应Command类的handle方法。所有的Command类都应该是django.core.management.base.BaseCommand的直接或间接子类。


原理搞清楚了，扩展manage命令就很容易了。创建一个app并加入到settings的INSTALLED_APPS中，在该app下面创建management.commands模块，并创建hello.py文件:

```python
from django.core.management.base import BaseCommand, CommandError
from django.db import models
#from placeholders import *
import os
  
class Command(BaseCommand):
   def handle(self, *args, **options):
     print 'hello, django!'
```

就可以使用hello命令了:
```
$ python manage.py hello
hello, django!
```

复制粘贴结束了，那么其实扩展manage.py就只需要在management----commands目录下新建文件夹并引入basecommands即可。
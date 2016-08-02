# study
学习用分支


permutation.py：排列组合分组实现

wxhongbao.py：微信红包算法Python实现

interview.py: 一道有趣的面试题（有未解决的疑惑）

send_post.py: POST接口测试工具


===============================================
Django_login.py:

用户的身份验证过程：
1. 首先通过 authenticate() 方法对传入的用户名、密码等信息进行验证，如果符合，则返回相应的 user 对象，同时，该方法会对 user 对象加以标注，通过附加 user.backend 属性来记录验证是被哪个配置的 backend 通过的。默认只有一个 backend，是 django.contrib.auth.backends.ModelBackend.
2. login 方法调用
    如果上一步身份验证通过，则此方法中对 request.session 中简单的添加两个键值：
    (1) "_auth_user_id"  这个是 user.id
    (2) "_auth_user_backend" 这个是 user.backend

因此只要给DJango一个user对象和user.id,user.backend就可以实现任意用户不用密码改变登录态
=================================================

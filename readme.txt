这本书教程有点问题   引入的时候引入方式不应该是from flask.ext.script import Manager  应该是  from flask_script import Manager  否则会出现各种问题

### flask学习

今天在自定义404错误页面的时候怎么也出不来自定义的界面，后来发现是启动服务器的时候有问题，应该用普通的启动方式
> python hello.py runserver

不应该用带参数的manage的形式的打开方式

> python hello.py runserver -h 0.0.0.0


(换了之后才发现用原来的方法也是可以的，不知道是缓存还是什么的原因)
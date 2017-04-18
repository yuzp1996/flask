这本书教程有点问题   引入的时候引入方式不应该是from flask.ext.script import Manager  应该是  from flask_script import Manager  否则会出现各种问题
***
出现错误


flask_sqlalchemy\__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
  warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')


参考

http://blog.csdn.net/qq_25730711/article/details/53690687
***

注意位置


app = Flask(__name__)

manager = Manager(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
***


### flask学习

今天在自定义404错误页面的时候怎么也出不来自定义的界面，后来发现是启动服务器的时候有问题，应该用普通的启动方式
> python hello.py runserver

不应该用带参数的manage的形式的打开方式

> python hello.py runserver -h 0.0.0.0


(换了之后才发现用原来的方法也是可以的，不知道是缓存还是什么的原因)
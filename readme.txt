�Ȿ��̳��е�����   �����ʱ�����뷽ʽ��Ӧ����from flask.ext.script import Manager  Ӧ����  from flask_script import Manager  �������ָ�������
***
���ִ���


flask_sqlalchemy\__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
  warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')


�ο�

http://blog.csdn.net/qq_25730711/article/details/53690687
***

ע��λ��


app = Flask(__name__)

manager = Manager(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
***


### flaskѧϰ

�������Զ���404����ҳ���ʱ����ôҲ�������Զ���Ľ��棬����������������������ʱ�������⣬Ӧ������ͨ��������ʽ
> python hello.py runserver

��Ӧ���ô�������manage����ʽ�Ĵ򿪷�ʽ

> python hello.py runserver -h 0.0.0.0


(����֮��ŷ�����ԭ���ķ���Ҳ�ǿ��Եģ���֪���ǻ��滹��ʲô��ԭ��)
from flask import request
from flask import abort
from flask_script import Manager, Shell
from flask import Flask, render_template
from flask import redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_mail import Mail
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TRARDOWN'] = True
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

class NameForm(Form):
    name = StringField('What is Your Name', validators=[Required()])
    password = StringField('Please input your password', validators=[Required()])
    submit = SubmitField('Submit')



manager = Manager(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'
migrate = Migrate(app, db)
mail = Mail(app)
manager.add_command('db', MigrateCommand)





# @app.route('/')
# def index():
# 	return render_template('index.html', current_time = datetime.utcnow())


# @app.route('/', methods=['GET','POST'])
# def index():
# 	name = None
# 	form = NameForm()
# 	if form.validate_on_submit():
# 		name = form.name.data
# 		form.name.data = ''
# 	return render_template('index.html', form=form, name = name, current_time = datetime.utcnow())




# @app.route('/', methods=['GET','POST'])
# def index():
# 	form = NameForm()
# 	if form.validate_on_submit():
# 	    session['name'] = form.name.data
# 	    return  redirect(url_for('index'))
# 	return render_template('index.html', form=form, name = session.get('name'), current_time = datetime.utcnow())




# @app.route('/', methods=['GET','POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         if old_name is not None and old_name != form.name.data:
#             flash('Look like you have changed your name!')
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name = session.get('name'), current_time = datetime.utcnow())

    
    


# @app.route('/')s
# def index():
# 	user_agent = request.headers.get('User-Agent')
# 	return '<p>Your Browser Is %s</p>' % user_agent


# @app.route('/user/<name>')
# def user(name):
# 	if not name:
# 		abort(404)
# 	return '<h1>hello, %s!</h1>' % name
	# return redirect('http://www.baidu.com')

# @app.route('/')
# def index():
# 	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name = name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404



    
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Role %r>' % self.name
    users = db.relationship('User', backref = 'role')
        
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True,index=True)

    def __repr__(self):
        return '<User %r>' % self.username        
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    


# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)
# manager.add_command("shell",Shell(make_context=make_shell_context()))

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        print 1
        print form.name.data
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name = session.get('name'), current_time = datetime.utcnow())
    


if __name__ == '__main__':
	# app.run(debug = True)
	manager.run()




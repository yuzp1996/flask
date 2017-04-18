
from flask import request
from flask import abort
from flask_script import Manager
from flask import Flask, render_template	
from flask import redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('What is Your Name', validators=[Required()])
	password = StringField('Please input your password', validators=[Required()])
	submit = SubmitField('Submit')


app = Flask(__name__)
manager = Manager(app)

bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'


 
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




@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Look like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name = session.get('name'), current_time = datetime.utcnow())

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





if __name__ == '__main__':
	app.run(debug = True)
	# manager.run()




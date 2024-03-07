from datetime import datetime
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/user/<nome>/<pront>/<inst>')
def ident(nome, pront, inst):

    return render_template('ident.html', pront = pront, nome = nome, inst = inst)

@app.route('/contextorequisicao/<nome>')
def reqcontext(nome):
    host_address = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    browser_data = request.host_url

    return render_template('reqcontext.html', host_address=host_address, remote_ip=remote_ip, browser_data=browser_data, nome = nome)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

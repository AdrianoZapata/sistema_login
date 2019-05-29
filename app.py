from bottle import Bottle, route, run
from bottle import request, template
from bottle import static_file, get
from bottle import error
'''
@route('/')
@route('/user/<nome>')
def index(nome='Unknown'):
	return '<center><h1>Look how awesome you are</h1>' + nome + '</h1></center>'

@route('/artigo/<id>')
def artigo(id):
	return '<h1> You are reading my article' + id + '</h1>'

@route('/pagina/<id>/<nome>')
def pagina(id, nome):
	return '<h1> You are checking my newest work ' + id + ' with name ' + nome + '</h1>'
'''
# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg/png/gif/ico)>')
def stylesheets(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot/ttf/woff/svg)>')
def stylesheets(filename):
	return static_file(filename, root='static/fonts')

@route('/login') # @get('/login')
def login():
	return template('login')

def check_login(username, password):
	d = {'adriano':'python', 'jhon':'java', 'peter':'go'}
	if username in d.keys() and d[username] == password:
		return True
	else:
		False

@route('/login', method='POST') # @post('/login')
def acao_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	sucesso = check_login(username, password)
	return template('verificao_login', sucesso=check_login(username,password), nome=username)

@error(404)
def error404(error):
	return template('page404')
	

if __name__ == '__main__':
	run(host='localhost', port=8080, debug=False, reloader=True)
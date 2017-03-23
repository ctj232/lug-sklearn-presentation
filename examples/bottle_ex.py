from bottle import route, run, template

@route('/hello/<name>')
def hello(name):
    return '<h1>Hello {name}!</h1>'.format(name)

run(host='localhost', port=8080)

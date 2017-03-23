@route('/hello/<name>')
def hello(name):
    return '<h1>Hello {name}!</h1>'.format(name)

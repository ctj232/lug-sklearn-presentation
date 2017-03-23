@route('/introduce/<name>')
def introduce(name):
    response.set_cookie('name', name)
    return 'Nice to meet you!'

@route('/welcomeback')
def welcomeback():
    name = request.cookies.get('name', 'Stranger')
    return 'Welcome back, {}!'.format(name)

from bottle import route, static_file

@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

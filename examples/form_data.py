@post('/login')
def login_user():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if login_ok(username, password):
        return 'Congrats! You broke in!'
    else:
        return 'Better luck next time.'

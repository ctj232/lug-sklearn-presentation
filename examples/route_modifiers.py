@route('/user/<uid:int>')
def user_by_id(uid):
    # ... load up a user by id

@route('/user/<username:re:[a-z]+>')
def user_by_name(username):
    # ... load up a user by name

@error(403)
def error403(error):
    return "You're not allowed in here."

@error(404)
def error404(error):
    return "It's not my fault."

@error(500)
def error500(error):
    return "I made a mistake."

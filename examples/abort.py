@route('/pages/<pagename>')
def load_page(pagename):
    if pagename not in pages:
        abort(404, "This page does not exist")
    # ...

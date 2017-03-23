@route('/pages/<pagename>')
def load_page(pagename):
    if pagename not in pages:
        redirect('/newpage')
    # ...

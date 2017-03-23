@route('/')
@route('/page/<pagename>')
def wiki_page(pagename='FrontPage'):
    # ... load page from database and return it

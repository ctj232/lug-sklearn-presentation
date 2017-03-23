@route('/page/<pagename>')
def wiki_page(pagename='FrontPage'):
    # ... load up a wiki page

@route('/<username>/<pagename>')
def user_page(username, pagename):
    # ... load up a user's personal page

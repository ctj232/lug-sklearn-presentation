@route('/')
def home():
    # ...

# make another bottle app
blog = Bottle()

@blog.route('/')
def blog_home():
    # ...

# /blog accesses all in the blog app
# you can use any WSGI-compatible app here
default_app().mount('/blog', blog)

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Chalt'}
    return '''
<html>
    <head>
        <title>Home Page - Tutorial</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
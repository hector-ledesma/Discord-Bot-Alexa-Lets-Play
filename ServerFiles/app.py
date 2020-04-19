#We have to import all library functions that we will want to use.
from flask      import Flask, render_template, url_for, request, redirect, abort
#Flask is the class template that we will instantiate.
#Request lets us handle differnet HTTP Methods to the same route.

# HTTP Mthod properties.
get     = 'GET'
post    = 'POST'

app = Flask(__name__)

@app.route('/', methods=[post, get])
def welcome():
    if request.method == get:
        print('Hello world!')
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
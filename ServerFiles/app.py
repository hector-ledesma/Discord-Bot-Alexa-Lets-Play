#We have to import all library functions that we will want to use.
from flask          import Flask, render_template, url_for, request, redirect, abort, jsonify
#Flask is the class template that we will instantiate.
#Request lets us handle differnet HTTP Methods to the same route.

# HTTP Mthod properties.
get     = 'GET'
post    = 'POST'

app = Flask(__name__)

# GLOBAL PROPERTY -------------
# do_something = False

# FLASK ---------------------------

@app.route('/', methods=[post, get])
def welcome():
    if request.method == get:
        print('Hello world!')
    
    return render_template('index.html')

@app.route('/_bot_test')
def send_message_to_client():
    print(request.args.get('msg', 0, type=str))
    return jsonify(result='Successfully transferring data from server to bot.')

@app.route('/_add_numbers')
def add_numbers():
    print('received request.')
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    print(a+b)
    return jsonify(result=a + b, user= 'Emil', worse= 'Shin')


if __name__ == "__main__":
    app.run(debug=True)
#We have to import all library functions that we will want to use.
from flask          import Flask, render_template, url_for, request, redirect, abort, jsonify
from flask_socketio import SocketIO, emit, send
import eventlet
eventlet.monkey_patch()
#Flask is the class template that we will instantiate.
#Request lets us handle differnet HTTP Methods to the same route.

# HTTP Mthod properties.
get     = 'GET'
post    = 'POST'

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
clients = []

# FLASK ---------------------------

@app.route('/', methods=[post, get])
def welcome():
    if request.method == get:
        print('Hello world!')
    
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    print('Client connected')
    clients.append(request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    clients.remove(request.sid)

@app.route('/_bot_test')
def send_message_to_client():
    print(request.args.get('msg', 0, type=str))
    socketio.send("my response", {'data' : 'testing'}, broadcast=True)
    return jsonify(result='Successfully transferring data from server to bot.')


@socketio.on('alexasaid')
def handlethisshit(msg):
    print(' do we make it here?????????????????????????????????????????? ')
    socketio.emit('handle alexa', "data to client")
    # return jsonify(result='Testing ...')


@app.route('/_add_numbers')
def add_numbers():
    print('received request.')
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    print(a+b)
    return jsonify(result=a + b, user= 'Emil', worse= 'Shin')

# tHIS IS AN EVENT CALLBACK. This listens for then 'my event' is triggered.
@socketio.on('my event')
def test_message(json):
    print('received json: ' + str(json))
    emit('my response', {'data': 'got it!'})

@socketio.on('message')
def handle_message(message):
    print('message trigerred')
    

@socketio.on('json')
def handle_json(json):
    print(json)
    send(json, json=True)




if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app)
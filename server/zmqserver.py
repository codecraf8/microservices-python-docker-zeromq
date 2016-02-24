# server.py
import time
import zmq

HOST = '127.0.0.1'
PORT = '4444'

_context = zmq.Context()
_publisher = _context.socket(zmq.PUB)
url = 'tcp://{}:{}'.format(HOST, PORT)


def publish_message(message):

    try:
        _publisher.bind(url)
        time.sleep(1)
        print "sending message : {0}".format(message, _publisher)
        _publisher.send(message)

    except Exception as e:
        print "error {0}".format(e)

    finally:
        print "unbinding"
        _publisher.unbind(url)


from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/downcase/", methods=['GET'])
def lowerString():

    _strn = request.args.get('param')
    response = 'lower case of {} is {}'.format(_strn, _strn.lower())
    publish_message(response)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

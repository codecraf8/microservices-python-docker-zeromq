#### 1. Build the publisher first

`sudo docker build -t docker-zmq-pub .`

`docker run --name docker-pub-server -p 5000:5000 -p 4444:4444 -t docker-zmq-pub`

#### 2. Run the Client

`python zmqclient.py`

Make a request to `localhost:5000/downcase/?Param=<String with mixed case letters>`

Messages from publisher will be sent over to subscriber.

Additonally, it logs to a file called subscriber.log

You can read more about it [here](http://blog.apcelent.com/how-to-setup-microservices-python-zeromq-docker-example.html).

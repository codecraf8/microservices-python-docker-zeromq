#### 1. Build the publisher first

sudo docker build -t docker-zmq-pub .
docker run --name docker-pub-server -p 5000:5000 -p 4444:4444 -t docker-zmq-pub

#### 2. Run the Client

python zmqclient.py

Make a request to localhost:5000/downcase/?Param=Hello

Messages from publisher will start to get recorded in the client.
Additonally if the client runs as a daemon, it logs to a file called sibscriber.log

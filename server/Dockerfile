FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y --force-yes python python-dev python-setuptools software-properties-common gcc python-pip
RUN apt-get clean all

RUN pip install pyzmq

RUN pip install Flask

ADD zmqserver.py /tmp/zmqserver.py

# Flask Port
EXPOSE 5000

# Zmq Sub Server
EXPOSE 4444

CMD ["python","/tmp/zmqserver.py"]

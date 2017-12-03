#!/bin/bash
cd /home/shiva
apt-get update
apt-get -y install python
apt-get -y install python-pip
apt-get -y install virtualenv
git clone https://github.com/shiv1994/cloudA3Request.git
cd cloudA3Request
virtualenv env
cd env
source bin/activate
cd ..
pip install locustio
locust --host=http://127.0.0.1:8000 --no-web -c 1000 -r 250 -n 600100

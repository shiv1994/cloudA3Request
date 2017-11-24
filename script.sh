sudo apt-get update
sudo apt-get -y python
sudo apt-get -y install python-pip
sudo apt-get -y install virtualenv
mkdir locustFolder
cd locustFolder
virtualenv env
cd env
source bin/activate
cd ..
pip install locustio
wget --no-check-certificate https://www.dropbox.com/s/rh4fmfg3039pzh9/helper.py?dl=0 -O helper.py
wget --no-check-certificate https://www.dropbox.com/s/hul4kyh4iai9reo/locustfile.py?dl=0 -O locustfile.py
locust --host=http://127.0.0.1:8000 --no-web -c 1000 -r 250

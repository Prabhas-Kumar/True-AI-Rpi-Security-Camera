sudo apt-get update
sudo apt-get -y dist-upgrade
sudo pip3 install virtualenv
python3 -m tflite1-env
source tflite1-env/bin/activate
bash get_pi_requirements.sh


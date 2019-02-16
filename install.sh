#!binbash
# A sample Bash installing script by Vaxure1337
echo "Installing LazySource"
echo -n -e  'sudo apt-get update'
echo -n -e  'sudo apt-get upgrade'
echo -n -e  'sudo apt-get install python'
echo -n -e  'sudo apt-get install python-pip'
echo -n -e  'sudo pip install pip-update'
echo -n -e  'sudo pip install -r requirements.txt'
echo -n -e  'sudo python setup.py install'
echo -n -e  'sudo python LazySource.py'

#!binbash
# A sample Bash installing script by Vaxure1337
echo "Installing LazySource"
sudo pip install -r requirements.txt
sudo python setup.py install
sudo python LazySource.py

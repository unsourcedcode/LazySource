#!binbash
# A sample Bash installing script by Vaxure1337
echo "Installing LazySource"
eval "sudo pip install -r requirements.txt"
eval "sudo python setup.py install"
eval "sudo python LazySource.py"

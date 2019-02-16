#!binbash
# A sample Bash installing script by Vaxure1337
echo "Installing LazySource"
cmd_install_requirements="sudo pip install -r requirements.txt"
eval $cmd_install_requirements
cmd_install_setup="sudo python setup.py install"
eval $cmd_install_setup
cmd_run="sudo python LazySource.py"
eval $cmd_run

#!binbash
# A sample Bash installing script by Vaxure1337
echo "Installing LazySource"
cmd_update="sudo apt-get update"
eval $cmd_update
cmd_upgrade="sudo apt-get upgrade"
eval $cmd_upgrade
cmd_install_python="sudo apt-get install python"
eval $cmd_install_python
cmd_install_python_pip="sudo apt-get install python-pip"
eval $cmd_install_python_pip
cmd_install_pip_update="sudo pip install pip-update"
eval $cmd_install_pip_update
cmd_install_requirements="sudo pip install -r requirements.txt"
eval $cmd_install_requirements
cmd_install_setup="sudo python setup.py install"
eval $cmd_install_setup
cmd_run="sudo python LazySource.py"
eval $cmd_run

from setuptools import setup

setup(
   name='LazySource',
   version='1.4.9',
   description='Pentesting Tools',
   long_description='LazySource is an pentesting tool for beginners',
   url='http://www.lazysource.gq/',
   author='Vaxure',
   author_email='vaxure@protonmail.com',
   zip_safe,
   include_package_data,
   install_requires=['gitpython', 'colorama', 'pathlib', "argparse"], #external packages as dependencies
)

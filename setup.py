from setuptools import setup

setup(
   name='LazySource',
   version='1.2',
   description='Tool',
   author='Vaxure',
   author_email='vaxure@protonmail.com',
   packages=['sqlmap', 'nmap'],  #same as name
   install_requires=['git', 'colorama', 'exchanges'], #external packages as dependencies
)

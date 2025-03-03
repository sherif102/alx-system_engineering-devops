#!/usr/bin/python3
"""fabfile to install mysql on servers"""
from fabric.api import run

env.hosts = ['3.94.86.136', '54.227.89.138']
env.user = 'ubuntu'

def install_mysql():
	"""install mysql"""
	run('sudo apt install mysql-server')

FROM ubuntu:14.04
MAINTAINER victor@tisnado.com
ENV DEBIAN_FRONTEND noninteractive

# update repositories
RUN sudo apt-get update -y
RUN sudo apt-get upgrade -y

# install Python
RUN sudo apt-get install -y python python-setuptools
RUN sudo easy_install pip

# install Virtualenv
RUN sudo pip install virtualenv
RUN mkdir -p /webapps/django/
RUN sudo virtualenv /webapps/django/
RUN cd /webapps/django
RUN sudo source bin/activate

# install Django
RUN sudo pip install django

# install Gunicorn
RUN sudo pip install gunicorn

# add Gunicorn configuration
ADD gunicorn_config.py /webapps/django/

# ******** ALERT: WORKING IN PROGRESS ************




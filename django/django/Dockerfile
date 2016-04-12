FROM ubuntu:14.04
MAINTAINER victor@tisnado.com
ENV DEBIAN_FRONTEND noninteractive

# update repositories
RUN sudo apt-get update -y
RUN sudo apt-get upgrade -y

# install Virtualenv
RUN sudo apt-get install -y python-virtualenv
RUN mkdir -p /webapps/django/
RUN sudo virtualenv /webapps/django/
RUN source /webapps/django/bin/activate

# install Django
RUN pip install django

# install Gunicorn
RUN pip install gunicorn

# add Gunicorn configuration
ADD gunicorn_config.py /webapps/django/

# ******** ALERT: WORKING IN PROGRESS ************


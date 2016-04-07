FROM ubuntu:14.04
MAINTAINER victor@tisnado.com
ENV DEBIAN_FRONTEND noninteractive

# update repositories
RUN sudo apt-get update -y
RUN sudo apt-get upgrade -y

# install Virtualenv
RUN apt-get install -y python-virtualenv
RUN sudo virtualenv /webapps/django/
RUN source /webapps/django/bin/activate

# install Django
RUN pip install django

# install Gunicorn
RUN pip install gunicorn

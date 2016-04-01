FROM ubuntu:14.04
MAINTAINER victor@tisnado.com
ENV DEBIAN_FRONTEND noninteractive

# update repositories / install curl and nano
RUN sudo apt-get update -y
RUN sudo apt-get install -y curl nano

# install Nginx, PHP and PHP-MySQL conector
RUN sudo apt-get install -y nginx php5-fpm php5-mysql

# change PHP FPM permissions 
RUN sed -i 's/;listen.mode/listen.mode/g' /etc/php5/fpm/pool.d/www.conf

# add logs directory and default site config
RUN mkdir -p /usr/share/nginx/logs
ADD default /etc/nginx/sites-available/

# expose port so server can be accesed via web
EXPOSE 80

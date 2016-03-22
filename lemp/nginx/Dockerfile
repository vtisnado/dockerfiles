FROM ubuntu
MAINTAINER victor@tisnado.com

# update repositories / install curl and nano
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get install -y curl nano

# install Nginx, PHP and PHP-MySQL conector
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get install -y nginx php5-fpm php5-mysql

# change PHP FPM permissions 
RUN sed -i 's/;listen.mode/listen.mode/g' /etc/php5/fpm/pool.d/www.conf

# add logs directory and default site config
RUN DEBIAN_FRONTEND=noninteractive mkdir /usr/share/nginx/html/logs
ADD default /etc/nginx/sites-available/
ADD index.php /usr/share/nginx/html/

# expose port so server can be accesed via web
EXPOSE 80

FROM ubuntu
MAINTAINER victor@tisnado.com

# update repositories / install curl and nano
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get update -y && \
DEBIAN_FRONTEND=noninteractive sudo apt-get install -y curl && \
DEBIAN_FRONTEND=noninteractive sudo apt-get install -y nano

# install Nginx and PHP
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get install -y nginx && \
DEBIAN_FRONTEND=noninteractive sudo apt-get install -y php5-fpm

# change PHP FPM permissions 
RUN sed -i 's/;listen.mode/listen.mode/g' /etc/php5/fpm/pool.d/www.conf

# add default site config
ADD default /etc/nginx/sites-available/
ADD index.php /usr/share/nginx/html/
RUN DEBIAN_FRONTEND=noninteractive mkdir /usr/share/nginx/html/logs

# expose port so server can be accesed via web
EXPOSE 80

# Build the image with the following command:
# docker build -t [IMAGE_NAME] [DOCKERFILE_PATH]
# Run the container with the following command:
# docker run -ti -p 80:80 [IMAGE_NAME] bash

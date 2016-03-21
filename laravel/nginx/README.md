
dockerfile-ubuntu-nginx
=======================
This image is based in Ubuntu 14.04
Build the image with the following command:

  $ docker build -t <image_name> <dockerfile_path>

Setup
=====
Run the container with the following command:

  $ docker run -ti -p 80:80 <image_name> bash

Launching Nginx
---------------
After the cointainer starts, you need to run the following commands so Nginx works with PHP-FPM:

  $ sudo service php5-fpm restart

  $ sudo service nginx start

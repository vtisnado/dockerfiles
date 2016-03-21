
dockerfile-ubuntu-nginx
=======================
This image is based in Ubuntu 14.04.

Build the image with this command:
```
$ docker build -t <image_name> <dockerfile_path>
```
Setup
=====
Run the container with the following command:
```
$ docker run -ti -p 80:80 <image_name> bash
```
Launching Nginx
---------------
After the cointainer start, run the following commands so PHP-FPM can detect the config changes:
```
$ sudo service php5-fpm restart
$ sudo service nginx start
```

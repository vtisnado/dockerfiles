
dockerfile-ubuntu-mysql
=======================
This image is based in Ubuntu 14.04.4

Build the image with this command:
```
$ docker build -t <image_name> <dockerfile_path>
```
Setup
=====
Run the container with the following command:
```
$ docker run -ti -p 3306:3306 <image_name> bash
```
Launching MySQL
---------------
After the container start, run the following commands to secure the MySQL installation
```
$ service mysql start
$ sudo mysql_secure_installation
```

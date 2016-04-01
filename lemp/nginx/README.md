
dockerfile-ubuntu-nginx
=======================
This image is based in Ubuntu 14.04.4

Build the image with this command:
```
$ docker build -t ubuntu_nginx <dockerfile_path>
```
Setup
=====
Run the container with the following command:
```
$ docker run -ti --name nginx --link mysql -p 80:80 -v /usr/docker/nginx:/usr/share/nginx ubuntu_nginx bash
```
Notice that you should run the mysql container first so the flag --link work.

Launching Nginx
---------------
After the cointainer start, run the following commands so PHP-FPM can detect the config changes:
```
$ sudo service php5-fpm restart
$ sudo service nginx start
```

Remember to exit with **CTRL/CMD + P + Q** so the container keep running in the background.


dockerfile-ubuntu-nginx
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
$ docker run -ti --name nginx --link mysql -p 80:80 -v /usr/share/nginx/html:/usr/share/nginx/html <image_name> bash
```
Notice that you should run the mysql container first so the --link work.

Launching Nginx
---------------
After the cointainer start, run the following commands so PHP-FPM can detect the config changes:
```
$ sudo service php5-fpm restart
$ sudo service nginx start
```

Remember to exit with CTRL/CMD + P + Q so the container keep running in the background.

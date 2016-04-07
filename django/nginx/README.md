
dockerfile-django-nginx
=======================
This image is based in Ubuntu 14.04.4

Build the image with this command:
```
$ docker build -t ubuntu_django_nginx <dockerfile_path>
```
Setup
=====
Run the container with the following command:
```
$ docker run -ti --name nginx -p 80:80 -v /usr/docker/nginx:/usr/share/nginx ubuntu_django_nginx bash
```

Launching Nginx
---------------
After the cointainer start, run the following command to start the Nginx service
```
$ sudo service nginx start
```

Remember to exit with **CTRL/CMD + P + Q** so the container keep running in the background.

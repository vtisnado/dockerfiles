
dockerfile-ubuntu-django-mysql
=======================
This image is based in Ubuntu 14.04.4

Build the image with this command:
```
$ docker build -t ubuntu_django_mysql <dockerfile_path>
```
Setup
=====
Run the container with the following command:
```
$ docker run -ti --name mysql -p 3306:3306 -v /usr/docker/mysql:/usr/docker/mysql ubuntu_mysql bash
```
Persistent data
===============
After the container start, run the following commands in order to change the mysql data directory to the server host.
```
cp -rap /var/lib/mysql /usr/docker/
chown -R mysql.mysql /usr/docker/mysql
mv /var/lib/mysql /var/lib/mysql_old
ln -s /usr/docker/mysql /var/lib/mysql
```

Launching MySQL
===============
Run the following commands to start the service and secure the MySQL installation
```
$ service mysql start
$ sudo mysql_secure_installation
```
Remember to exit with **CTRL/CMD + P + Q** so the container keep running in the background.


Connecting to MySQL server
==========================
Now you have to grant access to a MySQL user so you can connect from you PHP script in the nginx server:

```
GRANT ALL ON <database_name>.* TO <user>@'<django_container_ip>' IDENTIFIED BY '<password>';
```


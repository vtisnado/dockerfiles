Docker LEMP stack
=================
Here you can find the Dockerfiles to start a LEMP development enviroment using Nginx and PHP-FPM in one container and MySQL in another.

You will need to create the following directory in the host server in order to keep the database and other website files after each docker run or restart:

```
$ mkdir /usr/docker/
```

The docker container with Nginx will be linked to the MySQL container and both hava access to read and write persistent files in **/usr/docker/**

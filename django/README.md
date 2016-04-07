Docker Django-MySQL-Nginx stack
===============================
Here you can find the Dockerfiles to start a Django/Python development enviroment using three containers:

1. Django - Backend
2. MySQL - Database
3. Nginx - Static files

You will need to create the following directory in the host server in order to keep the database and other website files after each docker run or restart:

$ mkdir /usr/docker/
The docker container with Django will be linked to the MySQL container and both have access to read and write persistent files in /usr/docker/

FROM ubuntu:14.04
MAINTAINER victor@tisnado.com
ENV DEBIAN_FRONTEND noninteractive

# update repositories
RUN sudo apt-get update -y

# install MySQL
RUN sudo apt-get install -y mysql-server && \
sudo mysql_install_db

# change mysql default data directory
RUN sed -i 's/datadir=\/var\/lib\/mysql/datadir=\/usr\/docker\/mysql/g' /etc/mysql/my.cnf
RUN sed -i 's/socket=\/var\/lib\/mysql\/mysql.sock/socket=\/usr\/docker\/mysql\/mysql.sock/g' /etc/mysql/my.cnf

# allow connection from another server
RUN sed -i 's/bind-address/#bind-address/g' /etc/mysql/my.cnf

# expose port so server can be accesed via web
EXPOSE 3306

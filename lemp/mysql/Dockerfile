FROM ubuntu
MAINTAINER victor@tisnado.com

# update repositories
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get update -y

# install MySQL
RUN DEBIAN_FRONTEND=noninteractive sudo apt-get install -y mysql-server && \
DEBIAN_FRONTEND=noninteractive sudo mysql_install_db

# expose port so server can be accesed via web
EXPOSE 3306

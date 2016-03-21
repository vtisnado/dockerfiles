

Build the image with the following command:
$ docker build -t [IMAGE_NAME] [DOCKERFILE_PATH]

Run the container with the following command:
$ docker run -ti -p 80:80 [IMAGE_NAME] bash

After the cointainer starts, you need to run the following commands so Nginx works with PHP-FPM:
$ sudo service php5-fpm restart
$sudo service nginx start

#!/bin/bash

FOLDER_NAME=$1
ENV=$2

echo "
<VirtualHost *:80>

    Alias /static /home/ubuntu/$FOLDER_NAME/$FOLDER_NAME/static
    <Directory /home/ubuntu/$FOLDER_NAME/$FOLDER_NAME/static>
        Require all granted
    </Directory>

    Alias /media /home/ubuntu/$FOLDER_NAME/$FOLDER_NAME/media
    <Directory /home/ubuntu/$FOLDER_NAME/$FOLDER_NAME/media>
        Require all granted
    </Directory>

    <Directory /home/ubuntu/$FOLDER_NAME/$FOLDER_NAME/main/wsgi>
        <Files $ENV.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess $FOLDER_NAME python-home=/home/ubuntu/$FOLDER_NAME/venv python-path=/home/ubuntu/$FOLDER_NAME/$FOLDER_NAME
    WSGIProcessGroup $FOLDER_NAME
    WSGIScriptAlias / /home/ubuntu/$FOLDER_NAME/$FOLDER_NAME/main/wsgi/$ENV.py
    WSGIPassAuthorization On

    LogLevel info
    ErrorLog '${APACHE_LOG_DIR}'/$FOLDER_NAME.error.log
    CustomLog '${APACHE_LOG_DIR}'/$FOLDER_NAME.access.log combined

</VirtualHost>
"
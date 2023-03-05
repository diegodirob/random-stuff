#!/bin/bash

GREEN='\033[0;32m'
RED="\033[0;31m"
NC='\033[0m'

FOLDER_NAME=$1
ENV=$2

# Setup machine and install Apache
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

# Install essentials packages
sudo apt install libpq-dev python3-dev

# Install virtualenv
sudo pip3 install virtualenv

# CREATE APACHE CONF
sudo ~/path_to/apache.conf.generator.sh $FOLDER_NAME $ENV > /etc/apache2/sites-available/$ENV.conf

# ENABLE NEW CONF
sudo a2ensite $ENV.conf

read -p "Insert link to run git clone `echo $'\n> '`" LINK

# Verify LINK
if [ $LINK == "y" ]; then
    echo 1>&2 "${RED}$0: this field is required${NC}"
    exit 2
fi

# Clone project
echo "\n${GREEN}Cloning project${NC}"
git clone $LINK

# Set env
echo "\n${GREEN}Created virtual environment${NC}"
cd ~/$FOLDER_NAME
virtualenv venv
source venv/bin/activate

# Checkout branch
echo 'Pulling git repository'
git fetch
git checkout $ENV
git pull

# Install Reqs
read -p "-> Do you want install requirements (y/n)?`echo $'\n> '`" REQS
if [ $REQS == "y" ]; then
    pip install -r ~/$FOLDER_NAME/$FOLDER_NAME/requirements.txt
fi

# Complete Apache Configuration
cd ~/$FOLDER_NAME/$FOLDER_NAME
mkdir media
sudo chgrp www-data media 

echo 'Performing migrations'
export DJANGO_SETTINGS_MODULE="main.settings.$ENV"
python manage.py collectstatic
python manage.py migrate

# Run installtask command
read -p "-> Do you want run installtasks command (y/n)?`echo $'\n> '`" KRONOS
if [ $KRONOS == "y" ]; then
    python manage.py installtasks
fi

echo 'Updating Apache'
sudo systemctl restart apache2
sudo systemctl status apache2

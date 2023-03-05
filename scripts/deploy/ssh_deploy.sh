#!/bin/bash

GREEN='\033[0;32m'
RED="\033[0;31m"
NC='\033[0m'

FOLDER_NAME=$1
ENV=$2

echo '#### Pulling git repository'
cd ~/$FOLDER_NAME/
git fetch
git checkout $env
git pull

cd ~/$FOLDER_NAME/$FOLDER_NAME/
source ../venv/bin/activate

# Install Reqs
read -p "-> Do you want install requirements (y/n)?`echo $'\n> '`" REQS
if [ $REQS == "y" ]; then
    pip install -r requirements.txt
fi

echo 'Performing migrations'
export DJANGO_SETTINGS_MODULE="main.settings.$env"
python manage.py migrate
python manage.py installtasks

# Run installtask command
read -p "-> Do you want run installtasks command (y/n)?`echo $'\n> '`" KRONOS
if [ $KRONOS == "y" ]; then
    python manage.py installtasks
fi

echo 'Updating Apache'
sudo ~/path_to/apache.conf.generator.sh $FOLDER_NAME $ENV > /etc/apache2/sites-available/$ENV.conf
sudo systemctl restart apache2
sudo systemctl status apache2

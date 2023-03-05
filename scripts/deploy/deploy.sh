#!/bin/bash

GREEN='\033[0;32m'
RED="\033[0;31m"
NC='\033[0m'

# Verify parameters
if [ $# -lt 4 ]; then
  echo 1>&2 "${RED}$0: not enough arguments!`echo $'\n> '`sh deploy.sh ssh-key [staging|production] IP folder_name${NC}"
  exit 2
elif [ $# -gt 4 ]; then
  echo 1>&2 "${RED}$0: too many arguments!`echo $'\n> '`sh deploy.sh ssh-key [staging|production] IP folder_name${NC}"
  exit 2
fi

KEY=$1
ENV=$2
IP=$3
FOLDER_NAME=$4

echo "\n${GREEN}What do you want?${NC}"
echo "1 -> Setup flow, to deploy new application"
echo "2 -> Deploy flow, to update existing application"
echo "Other -> Terminate script"
read -p "Choose from the available options: 1 - 2 `echo $'\n> '`" OPT
if [ "$OPT" == "1" ]; then
    # SSH Connection
    echo "${GREEN}-> Start SSH connection${NC}"
    ssh ubuntu@"$IP" -i "$KEY" 'bash -s' < ~/path_to/ssh_setup.sh $FOLDER_NAME $ENV

    # Do stuff
fi

if [ "$OPT" == "2" ]; then
    # SSH Connection
    echo "${GREEN}-> Start SSH connection${NC}"
    ssh ubuntu@"$IP" -i "$KEY" 'bash -s' < ~/path_to/ssh_deploy.sh $FOLDER_NAME $ENV

    # Do other stuff
fi

echo "${GREEN}-> Script successfully executed ${NC}"

# Test to create a simple script that create-update-run a django basebackend for testing or simple tasks, skipping standard setup

GREEN='\033[0;32m'
NC='\033[0m'

ask_commands()
{
    echo "\n${GREEN}Do you want load some data?${NC}"
    read -p "Insert y to load or other to pass this point `echo $'\n> '`" command_check
    if [ "$command_check" == "y" ]; then
        python manage.py populate_db
    fi
}

echo "\n${GREEN}What do you want?${NC}"
echo "1, Create new baseback"
echo "2, Update my baseback"
echo "3, Run my baseback"
read -p "Choose from the available options: 1 - 2 - 3 `echo $'\n> '`" option
if [ "$option" == "1" ]; then
    echo "\n${GREEN}Cloning baseback project${NC}"
    git clone "https://baseback-endpoint/baseback.git"

    echo "\n${GREEN}Created virtual environment${NC}"
    cd "baseback"
    virtualenv venv -p python3
    source venv/bin/activate

    echo "\n${GREEN}Install requirements${NC}"
    pip install -r requirements.txt

    echo "\n${GREEN}Apply migrations and create superuser${NC}"
    cd "baseback"
    python manage.py migrate

    read -p "Do you want create a superuser? You can use it to login in Admin Panel `echo $'\n> '`" create_superuser
    if [ "$create_superuser" == "y" ]; then
        python manage.py createsuperuser
    fi

    ask_commands

    echo "\n${GREEN}Script completed successfully, running server.${NC}"
    python manage.py runserver 0.0.0.0:8000

    deactivate
fi

if [ "$option" == "2" ]; then
    echo "\n${GREEN}Pulling baseback project${NC}"
    cd "baseback"
    git pull

    echo "\n${GREEN}Activated virtual environment${NC}"
    source venv/bin/activate

    echo "\n${GREEN}Check for new packages${NC}"
    pip install -r requirements.txt

    echo "\n${GREEN}Check for new migrations${NC}"
    cd "baseback"
    python manage.py migrate

    ask_commands

    echo "\n${GREEN}Script completed successfully, running server.${NC}"
    python manage.py runserver 0.0.0.0:8000

    deactivate
fi

if [ "$option" == "3" ]; then
    cd "baseback"

    echo "\n${GREEN}Activated virtual environment${NC}"
    source venv/bin/activate

    cd "baseback"

    ask_commands

    echo "\n${GREEN}Running server.${NC}"
    python manage.py runserver 0.0.0.0:8000

    deactivate
fi

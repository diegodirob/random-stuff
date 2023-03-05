# Test to create a simple script that automatically creates a Django project ready to work

read -p "Insert project name: " project_name

if [ -z "$project_name" ]; then
  echo "Project name is required!"
  exit 1
fi

read -p "Insert base folder name, leave blank if you are already in the right folder: " folder_name
if [ "$folder_name" ]; then
  echo "Create new folder: $folder_name"
  mkdir $folder_name
  cd $folder_name
fi

echo "Create virtual environment"
virtualenv venv
source venv/bin/activate

echo "Install Django and run startproject"
python -m pip install Django
django-admin startproject main
mv main $project_name

echo "Created requirements.txt"
pip freeze > requirements.txt

cd $project_name
python manage.py migrate
python manage.py createsuperuser

read -p "Do you want install DRF? Insert yes to install " drf
if [ "$drf" == "yes" ]; then
  echo "Install Django REST Framework..."
  pip install djangorestframework
  pip install markdown
  pip install django-filter

  sed -i '' -e "39s/^//p; 39s/^.*/    'rest_framework',/" main/settings.py
  sed -i '' "17s/.*/from django.urls import path, include/" main/urls.py
  sed -i '' -e "20s/^//p; 20s/^.*/    path('api-auth\/', include('rest_framework.urls')),/" main/urls.py
fi

deactivate

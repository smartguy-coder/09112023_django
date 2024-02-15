# 09112023_django

poetry config --local virtualenvs.in-project true

docker-compose run --rm web-app sh -c "django-admin startproject library ."

poetry add psycopg2-binary 

docker-compose run --rm  web-app sh -c "python manage.py migrate"
docker-compose run --rm  web-app sh -c "python manage.py createsuperuser"
docker-compose run --rm  web-app sh -c "python manage.py runserver" 

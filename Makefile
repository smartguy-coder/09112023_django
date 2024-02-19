run:
	@echo 'Start server'
	echo 'Start server with command'
	docker-compose run --rm  web-app sh -c "python manage.py runserver"


migrations:
	docker-compose run --rm  web-app sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm  web-app sh -c "python manage.py migrate"

su:
	docker-compose run --rm  web-app sh -c "python manage.py createsuperuser"

newapp:
	docker-compose run --rm  web-app sh -c "python manage.py startapp $(app)"


shell:
	docker-compose run --rm  web-app sh -c "python manage.py shell"

run_file:
	@sh script_in_file.sh
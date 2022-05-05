install:
	docker-compose build

	docker-compose run web python ./manage.py migrate

	sudo chown -R $(USER):$(USER) .

change:
	sudo chown -R $(USER):$(USER) .

run:
	docker-compose up

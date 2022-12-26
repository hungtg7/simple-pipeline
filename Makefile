deploy:
	docker-compose down --rmi all -v --remove-orphans
	docker-compose up

run-services:
	docker network inspect kafka-network > /dev/null || docker network create kafka-network
	docker-compose -f docker-compose.kafka.yml up -d
	docker-compose up -d

stop-services:
	docker-compose down
	docker-compose.kafka.yml down
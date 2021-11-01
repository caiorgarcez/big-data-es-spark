run-services:
	docker network inspect kafka-network > /dev/null || docker network create kafka-network
	docker-compose -f docker-compose.kafka.yml up -d
	docker-compose up -d --build

run-kafka-services:
	docker network inspect kafka-network > /dev/null || docker network create kafka-network
	docker-compose -f docker-compose.kafka.yml up -d

stop-services:
	docker-compose down -v
	docker-compose -f docker-compose.kafka.yml down -v

stop-kafka-services:
	docker-compose -f docker-compose.kafka.yml down -v

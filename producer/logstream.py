import json
import os
from os.path import dirname, join
from time import sleep

from dotenv import load_dotenv
from kafka import KafkaProducer

from utils.get_log_from_file import get_raw_log_from_HDFS_application

dotenv_path = join(dirname(__file__), "./settings/.env.local")
load_dotenv(dotenv_path)

SLEEP_TIME = 1 / int(os.environ.get("TRANSACTIONS_PER_SECOND"))
log_count = int(os.environ.get("LOG_COUNT_INIT"))

if __name__ == "__main__":

    sleep(15)

    producer = KafkaProducer(
        bootstrap_servers=os.environ.get("KAFKA_BROKER_URL"),
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    while log_count < 1000:
        log_event: dict = get_raw_log_from_HDFS_application(log_count)
        producer.send(os.environ.get("TRANSACTIONS_TOPIC"), value=log_event)
        sleep(SLEEP_TIME)

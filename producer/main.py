import json
import os
from os.path import dirname, join
from time import sleep

from dotenv import load_dotenv

from handlers.streamHandler import StreamHandler
from utils.get_log_from_file import get_raw_log_from_HDFS_application

dotenv_path = join(dirname(__file__), "./settings/.env.local")
load_dotenv(dotenv_path)
log_count = int(os.environ.get("LOG_COUNT_INIT"))

# check user topic: docker-compose exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic raw_logs --from-beginning

if __name__ == "__main__":

    sh = StreamHandler()
    # sh.set_topic("raw_logs")
    producer = sh.get_producer()
    while log_count < 1000:
        log_count += 1
        log_event: dict = get_raw_log_from_HDFS_application(log_count)
        producer.send("raw_logs", value=log_event)
        sleep(4)

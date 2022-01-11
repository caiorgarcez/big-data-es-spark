import json
import os
from os.path import dirname, join
from time import sleep

from dotenv import load_dotenv

from handlers.streamHandler import StreamHandler
from utils.stream import get_last_msg_from_topic

dotenv_path = join(dirname(__file__), "./settings/.env.local")
load_dotenv(dotenv_path)
log_count = int(os.environ.get("LOG_COUNT_INIT"))

# check user topic: docker-compose exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic raw_logs --from-beginning

if __name__ == "__main__":
    sleep(4)
    sh = StreamHandler()
    consumer = sh.get_consumer("raw_logs")
    while log_count < 1000:
        log_count += 1
        if log_count % 2:
            msg = get_last_msg_from_topic(consumer)
            payload = msg.get("raw")
            print(f"message: {payload}")
        sleep(4)

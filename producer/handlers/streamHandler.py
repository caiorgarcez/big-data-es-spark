# from typing import List, Optional
import json
import os
from os.path import dirname, join
from time import sleep

from dotenv import load_dotenv
from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

dotenv_path = join(dirname(__file__), "../settings/.env.local")
load_dotenv(dotenv_path)

print(f"\n\n\n {os.environ.get('KAFKA_BROKER_URL')} ")

sleep(5)
class StreamHandler(object):
    def __init__(
        self,
    ) -> None:
        self.broker_url = os.environ.get("KAFKA_BROKER_URL")
        self.admin_client = KafkaAdminClient(
            bootstrap_servers=self.broker_url,
            client_id="anomaly",
            security_protocol="PLAINTEXT",
        )
        self.topic_list = list()

    def set_topic(self, topic_name):
        self.topic_list.append(NewTopic(name=topic_name, num_partitions=1, replication_factor=1))
        self.admin_client.create_topics(new_topics=self.topic_list, validate_only=False)

    def set_topic_for_new_user(self, user_uuid):
        consumer = KafkaConsumer(group_id="anomaly", bootstrap_servers=self.broker_url)
        curr_topics = consumer.topics()
        if user_uuid not in curr_topics:
            new_user_topic = [NewTopic(name=user_uuid, num_partitions=1, replication_factor=1)]
        self.admin_client.create_topics(new_topics=new_user_topic, validate_only=False)

    def get_producer(self):
        return KafkaProducer(
            bootstrap_servers=self.broker_url,
            # Encode all values as JSON
            value_serializer=lambda value: json.dumps(value).encode(),
        )

    def get_consumer(self, topic):
        return KafkaConsumer(
            topic,
            # group_id="lotier_concierge",
            group_id=None,
            auto_offset_reset="earliest",
            bootstrap_servers=self.broker_url,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            consumer_timeout_ms=1000,
        )


if __name__ == "__main__":
    sh = StreamHandler()
    sh.set_topics_for_users()

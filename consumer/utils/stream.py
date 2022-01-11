def get_last_msg_from_topic(consumer):
    consumer.poll()
    message = list()
    for msg in consumer:
        message.append(msg.value)
    return message[-1]

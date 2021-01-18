from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('names',
                         group_id='c1',
                         auto_offset_reset='earliest',
                         bootstrap_servers=['192.168.178.26:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8'))["value"])

for message in consumer:
    print("topic=%s "
          "partition=%d "
          "offset=%d "
          "key=%s "
          "value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))

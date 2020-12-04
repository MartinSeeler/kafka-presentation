from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import random

# read names.txt file
names = []
with open('names.txt', 'r') as f:
    for line in f:
    	names.append(str(line.strip()))
random.shuffle(names)

# connect to kafka
producer = KafkaProducer(
	bootstrap_servers=['localhost:9092'], 
	value_serializer=lambda m: json.dumps({"value": m}).encode('utf-8')
)

# send messages
for name in names:
	print(f"Sending {name}")
	producer.send('names', 
		#key=bytes(name[0], "utf-8"), 
		#key=bytes(str(len(name)), "utf-8"), 
		partition=0 if name[0]<="m" else 1,
		value=name)
	producer.flush()

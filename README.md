# Kafka Demo Playground

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install kafka-python
```

## Start Kafka 

```bash
$ docker-compose up -d

$ docker exec -t kafka-presentation_kafka_1 kafka-topics.sh --bootstrap-server :9092 --create --topic names --partitions 2 --replication-factor 1

$ docker exec -t kafka-presentation_kafka_1 kafka-topics.sh --create --bootstrap-server :9092 --topic names-compacted --replication-factor 1 --partitions 1 --config "cleanup.policy=compact" --config "delete.retention.ms=100" --config "segment.ms=100" --config "min.cleanable.dirty.ratio=0.01"

$ docker exec -t kafka-presentation_kafka_1 kafka-topics.sh --bootstrap-server :9092 --delete --topic names

$ docker exec -t kafka-presentation_kafka_1 kafka-topics.sh --bootstrap-server :9092 --delete --topic names-compacted
```
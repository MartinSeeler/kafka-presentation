slidenumbers: false


# Kafka<sub>1883 - 1924</sub>

# In a **Nutshell**

![](img/kafka.gif)

---

[.background-color: #FFFFFF]
![inline fit](img/ka_1.png)

^Kommunikation zum Daten senden, bspw MOnitoring
Daten sammeln, auswerten, neue Daten generieren

---

[.background-color: #FFFFFF]
![inline fit](img/ka_2.png)

^
Immer mehr services kommen dazu
immer mehr Verbindungen werden gezogen

---

[.background-color: #FFFFFF]
![inline fit](img/ka_3.png)

^
Technical-Debt wird zurückgezahlt
Single Service to provide infos is built
Pubsub messaging system is born
no direct sender/receiver

---

[.background-color: #FFFFFF]
![original fit](img/ka_4.png)

^
Andere machen das gleiche, schon wirds wieder komplex
Multiple Systems support
what you want single centralized system that allows for publishing generic types of data, which will grow as your business grows

---

[.header: #FFFFFF]
## Meet **Kafka**
![original](img/kafka.gif)

^
Message Broker / Streaming Platform zum Verteilen von Nachrichten
Sind persistent, geordnet und append-only
distributed commit log / distributing streaming platform
used by Spotify, Uber, Robinhood, Netflix, Sony

---

## producers **produce**

## consumers **consume**

### in large *distributed* reliable

### way and *realtime*

^
Im groben macht Kafka das


---

## **Topics** and 
## **Partitions**
## in Kafka

^
topics like a table in DBs
partitions is for redundancy, like shards in ES

---

## **Messages** in Kafka
### **~1 million** messages/s

^
data within Kafka is called a message
like a record in a DB
single producer / consumer
schema possible
no limits for data
size configurable

---

[.header: #FFFFFF]
## The core of Kafka
## is the **Log**
![original](img/log.gif)

---

### The *log* is simply a **time-ordered**, **append-only** sequence of data *inserts* where the *data* can be *anything*

---

[.background-color: #FFFFFF]
![inline](img/cons_1.png)

^
Bild von Topic
earliest, latest

---

[.background-color: #FFFFFF]
![original inline](img/part_1.png)

^
Partitions sind eigentliches log
beliebig erweitern aber nicht kleiner machen
verschiedene wege, das zu steuern
was bedeutet das für ordering?
ordering ist also nur in Partition gegeben!

---

[.background-color: #FFFFFF]
# **1** Consumer from **1** group
![inline](img/topics_1.png)

^
wenn nur 1 consumer, dann übernimmt er alle partitionen

---

[.background-color: #FFFFFF]
# **2** Consumers from **1** group
![inline](img/topics_2.png)

^
2 consumer teilen sich rein

---

[.background-color: #FFFFFF]
![original inline](img/cons_group_offsets.png)


---

[.background-color: #FFFFFF]
# **4** Consumers from **1** group
![inline](img/topics_3.png)

^
ab 4 consumern hat jede partition einen consumer
aber was passiert danach?

---

[.background-color: #FFFFFF]
# **5** Consumers from **1** group
![inline](img/topics_4.png)

^
consumer ist idle und bekommt keine nachrichten
wichtig für partitionen, können nur erweitert aber nicht reduziert werden

---

[.background-color: #FFFFFF]
# **2** Consumer groups
![inline](img/topics_5.png)

^
rebalancing when consumer gets added or removed
analogie zu subscriber
bspw versch. services

---

[.header: #FFFFFF]
## Where will it go?
![original](img/wondering.gif)

---

## when nothing is specified, **round robin** behaviour is used

---

## when only a **key** is specified, partition is choosen based on 
## **hash of the key**

---

## If a valid **partition number** is specified, that **partition** will be used

---

[.header: #FFFFFF]
## **Redundancy** in Kafka
![original](img/trumps.gif)

---

[.background-color: #FFFFFF]
![inline](img/part_sharding.jpeg)

^
Leader distributed

---

## To tolerate **N** *failures*, you need **2N+1** *replicas*

---

[.header: #FFFFFF]

## **Costs** and **Infrastructure**

![original](img/money.gif)

^
Downside von Kafka
kann man nicht gegen null laufen lassen
cloud und functions spielen einfacher zusammen
zookeeper

---

## **Alternatives** to Kafka

^
Amazon AWS Kinesis is a managed version of Kafka whereas I think of Google Pubsub as a managed version of Rabbit MQ. Amazon SNS with SQS is also similar to Google Pubsub (SNS provides the fanout and SQS provides the queueing).

---

## Customizable
## **Data Retention**

^
vorteile von Kafka
disk based retention, long duration
by time, messages, bytes
higher level aggregations
offsets erklären, laufen die nicht aus?
1TB/d -> 4 mio days

---

## Meet **KSQL**

```sql
CREATE TABLE pageviews_per_region_per_minute AS
  SELECT regionid,
         count(*)
  FROM pageviews_enriched
  WINDOW TUMBLING (SIZE 1 MINUTE)
  GROUP BY regionid
  EMIT CHANGES;
```

---

[.header: #FFFFFF]

## Any **Questions**?

![original](img/questions.gif)


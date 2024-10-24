## Preliminaries

### Pull images from both compose files

`docker-compose -f docker-compose-kafka.yml pull`

`docker-compose -f docker-compose-mqtt.yml pull`

### Install the python dependencies

`pip install -r src/requirements.txt`

## MQTT stack

### Run the mqtt stack

`docker-compose -f docker-compose-mqtt.yml up`

Optionally we can run the [mqtt explorer](https://mqtt-explorer.com/) to watch the broker's content.

### Run the producer

`python src/mqtt/producer.py`

In the explorer we can view the new messages that pass through the topic

### Run the consumer

`python src/mqtt/consumer.py`


## Kafka stack

### Run the mqtt stack

`docker-compose -f docker-compose-kafka.yml up`

Together with the kafka stack we deploy an explorer so that we can watch the broker's content. The explorer is available at `localhost:9007`.

### Run the producer

`python src/kafka/producer.py`

In the explorer we can view the new messages that pass through the topic

### Run the consumer

`python src/kafka/consumer.py`

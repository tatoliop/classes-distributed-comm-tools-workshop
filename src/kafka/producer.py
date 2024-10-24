import time

from confluent_kafka import Producer

if __name__ == "__main__":
    # Conf for kafka connection
    conf = {'bootstrap.servers': 'localhost:9092','client.id': 'myproducer'}
    # Create the producer
    producer = Producer(conf)
    # Topic var
    topic = 'mytopic'
    # Create the msg
    msg = f'Current time is {time.time()}'
    while True:
        # Publish the msg
        print(f'Publishing: {msg}')
        producer.produce(topic, msg)
        # Wait 5 seconds and publish again
        time.sleep(5)

# 生产端
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka1:9092'])
future = producer.send('test', value=b'my_value', partition=0)
result = future.get(timeout= 100)
print(result)
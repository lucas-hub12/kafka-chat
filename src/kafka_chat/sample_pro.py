from kafka import KafkaProducer
import time
from tqdm import tqdm
import json

producer = KafkaProducer(
        bootstrap_servers='3.34.3.97:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

for i in tqdm(range(10000)):
    msg = { "msg" : str(i) }  
    # f'message {i}'.encode('utf-8')
    
    producer.send('test-topic',msg)
    # producer.flush()
    # 100 개 단위로 나눠서 flush()하기
    if i % 100 == 0 :
        producer.flush()
    time.sleep(0.01)
producer.flush()

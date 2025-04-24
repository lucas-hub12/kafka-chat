# src/kafka_chat/chatthread.py

from kafka import KafkaConsumer, KafkaProducer
from threading import Thread
import json

def receive_messages(user: str, topic: str, bootstrap: str):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap,
        group_id=f"group-{user}",
        auto_offset_reset="latest",
        enable_auto_commit=False
    )

    for msg in consumer:
            try:
                data = json.loads(msg.value.decode('utf-8'))
                print(f"💬 {data['user']}: {data['msg']}")
            except Exception as e:
                print(f"[오류] 메시지 디코딩 실패: {msg.value}, 에러: {e}")

def run_chat_thread_topic():
    user = input("👤 내 이름: ")
    topic = input("🧵 토픽 이름 (예: chat-a-to-b): ")
    bootstrap = input("🌐 Kafka 서버 주소 (예: 3.34.3.97:9092): ")

    producer = KafkaProducer(bootstrap_servers=bootstrap)

    # 수신 쓰레드 시작
    thread = Thread(target=receive_messages, args=(user, topic, bootstrap), daemon=True)
    thread.start()

    print("\n📥 채팅 시작! (exit 입력 시 종료)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        message = json.dumps({"user": user, "msg": user_input})
        producer.send(topic, message.encode("utf-8"))
        

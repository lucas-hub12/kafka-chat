from kafka import KafkaProducer
import time

def run_chat_producer():
    print("채팅 프로그램 - 메시지 발신자")
    bootstrap_servers = input("🛠 Kafka 서버 주소 (예: 퍼블릭 IPv4 주소:9092): ").strip()
    topic = input("📦 토픽 이름: ").strip()

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    print("\n메시지를 입력하세요 (종료하려면 'exit' 입력)\n")

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            print("🚪 채팅을 종료합니다.")
            break

        producer.send(topic, msg.encode('utf-8'))
        producer.flush()

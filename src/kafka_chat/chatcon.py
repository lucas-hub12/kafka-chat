from kafka import KafkaConsumer

def run_chat_consumer():
    print("채팅 프로그램 - 메시지 수신자")
    bootstrap_servers = input("Kafka 서버 주소 입력 (예: localhost:9092): ").strip()
    topic = input("토픽 이름 입력: ").strip()
    group_id = input("Consumer Group ID 입력 (예: chat-group): ").strip()

    print("\n📥 메시지 수신 대기 중... (Ctrl+C로 종료)\n")
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id=group_id,
        auto_offset_reset='latest',
        enable_auto_commit=False
    )

    try:
        for message in consumer:
            print(f"💬 {message.value.decode('utf-8')}")
    except KeyboardInterrupt:
        print("👋 종료합니다.")
        consumer.close()

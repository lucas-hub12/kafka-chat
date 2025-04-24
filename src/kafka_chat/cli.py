from kafka_chat.chatpro import run_chat_producer
from kafka_chat.chatcon import run_chat_consumer

def main():
    mode = input("모드 선택 (send / recv): ").strip().lower()
    if mode == 'send':
        run_chat_producer()
    elif mode == 'recv':
        run_chat_consumer()
    else:
        print("❌ 잘못된 입력입니다. 'send' 또는 'recv'를 입력하세요.")

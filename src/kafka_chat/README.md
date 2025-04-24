# Kafka Chat Program

## Repo 및 Pr 
```bash
$ mkdir ~/code/kafka-chat
$ cd ~/code/kafka-chat
$ pdm init
$ source .venv/bin/activate
$ pdm add tqdm kafka-python
$ pdm list
$ git init
$ git remote add origin https://github.com/lucas-hub12/kafka-chat.git
$ git add .
$ git commit -m "init: 프로젝트 초기 설정"
$ git push -u origin main
$ git checkout -b 0.2.0/chatpro
$ git push
``` 
## Ready  
```bash
$ pdm init
$ source .venv/bin/activate
$ pdm add tqdm kafka-python
$ pdm list
$ vi src/kafka_chat/cli.py # 생성
$ vi src/kafka_chat/chatpro.py # 생성
$ vi src/kafka_chat/chatcon.py # 생성
$ vi pyproject.toml # 요구 사항 추가
$ $ pdm install
```

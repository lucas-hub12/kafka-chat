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
## cli 를 위한 코드
- pyproject.toml 추가
```bash
[tool.pdm]
distribution = true
packages = [{ include = "kafka_chat", from = "src" }]

[project.scripts]
chatpro = "kafka_chat.cli:main"
chatcon = "kafka_chat.chatcon:run_chat_consumer"
```
- 추가 반영 실행 코드
```bash
pip install -e .
```
## 실행 화면
![image](https://github.com/user-attachments/assets/94754857-611a-4534-ac65-18a5300027ad)

![image](https://github.com/user-attachments/assets/04cbbe17-bcb8-493a-a666-236ca8984d0b)


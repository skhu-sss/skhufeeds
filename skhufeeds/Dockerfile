FROM python:latest

# 앱 디렉터리 생성
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# 서버측 소스코드 복사
COPY . /usr/src/app

# 의존성 설치 - Python 모듈 패키지
RUN apt update -y && apt install -y mysql-client libmysqlclient-dev \
  && pip3 install -r requirements.txt

# 3000 번 포트 노출
EXPOSE 3000

# 실행 명령
CMD bash start_main.sh

FROM alpine:3.7

MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>
RUN apk update --no-cache && apk add python3 \
python3-dev \
py3-pip \ 
git \
bash

RUN git clone https://github.com/blabla1337/skf-workshop-py5.git
WORKDIR /skf-workshop-py5/target
RUN pip3 install -r requirements.txt
CMD [ "python3", "./runserver.py" ]
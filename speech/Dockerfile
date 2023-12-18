FROM ubuntu:latest

RUN apt update
RUN apt install -y python3-pip

WORKDIR /dst

COPY ./mail-ftp.py /dst/mail-ftp.py

CMD [ "python3", "mail-ftp.py" ]
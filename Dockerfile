# Written by Mateusz Rzeczyca
# info@mateuszrzeczyca.pl
# 13.03.2020

FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

CMD ["python3", "./server.py"]

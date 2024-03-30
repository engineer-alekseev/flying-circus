FROM python:3.11                                                                                                                                

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update;                     \
    apt-get upgrade -y;                 \
    apt-get install -y libcairo2-dev;   \
    apt-get -y autoclean;               \
    apt-get -y autoremove;

RUN python3 -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

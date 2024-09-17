FROM python:3.11.9

WORKDIR /app

COPY  requirement.txt ./

RUN pip install -r requirements.txt

COPY . .


# app/Dockerfile

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

ADD ./requirements.txt /app/

RUN pip3 install -r requirements.txt

ADD . /app/

EXPOSE 8500

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8500", "--server.address=0.0.0.0"]
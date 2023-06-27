FROM python:3.11

WORKDIR /root

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
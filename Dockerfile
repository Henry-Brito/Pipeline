FROM python:3.10

WORKDIR /media_devops
COPY . .

RUN pip install -f requirements.txt

CMD [ "python", "media_devops.py" ]
FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY composer_guardian.py /app

CMD [ "python", "./composer_guardian.py" ]

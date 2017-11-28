FROM python:2.7

WORKDIR /app

EXPOSE 5000

ENV NAME World

CMD ["python", "app.py"]

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD app.py /app/app.py

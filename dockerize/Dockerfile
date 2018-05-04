FROM python:2.7

WORKDIR /app

EXPOSE 5000

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD app.py /app/app.py
CMD ["python", "app.py"]

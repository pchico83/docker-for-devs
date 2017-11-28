FROM alpine:3.1

RUN apk add --update python py-pip

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]

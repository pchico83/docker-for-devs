FROM alpine:3.1

RUN apk add --update python py-pip

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

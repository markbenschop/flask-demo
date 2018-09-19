FROM alpine:3.8
MAINTAINER Mark Benschop "mark@benschop.tech"
RUN apk add python3 py-pip && python3 -m ensurepip && pip install --upgrade pip && pip install flask
# RUN easy_install pip
COPY templates /app
WORKDIR /app
COPY . /app/
ENTRYPOINT ["python"]
CMD ["app.py"]

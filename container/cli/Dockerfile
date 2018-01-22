FROM python:alpine
MAINTAINER Roel Harbers <roelharbers@gmail.com>

RUN apk add --no-cache \
    gcc \
    libffi-dev \
    openssl-dev \
    musl-dev \
;

WORKDIR /usr/local/src/binance/cli
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY bin bin
COPY binance_cli binance_cli
COPY tests tests
COPY util util

ENTRYPOINT ["bin/binance"]
CMD ["--help"]

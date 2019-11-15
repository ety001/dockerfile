FROM alpine:3.9

RUN apk add --no-cache python3 gcc python3-dev musl-dev openssl-dev && \
    pip3 install bitshares && \
    apk del gcc python3-dev musl-dev openssl-dev

RUN pip3 install --upgrade bitshares

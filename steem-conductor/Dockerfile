FROM alpine:3.6
RUN apk add --no-cache python3 python3-dev gcc git musl-dev libffi-dev openssl-dev \
    && pip3 install -U git+git://github.com/Netherdrake/steem-python \
    && pip3 install -U git+https://github.com/Netherdrake/conductor \
    && apk del git gcc musl-dev libffi-dev python3-dev
ENV UNLOCK=123456
CMD ["conductor"]

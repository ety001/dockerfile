FROM alpine:3.7
RUN apk add --no-cache python3 python3-dev gcc g++ git musl-dev libffi-dev openssl-dev \
    && pip3 install steem \
    && apk del git gcc g++ musl-dev libffi-dev python3-dev
CMD ["steempy"]

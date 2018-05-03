FROM alpine:3.6
RUN apk add --no-cache python3 python3-dev gcc git musl-dev libffi-dev openssl-dev \
    && pip3 install steem
CMD ["steempy"]

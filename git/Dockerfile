FROM alpine:latest

RUN apk --no-cache add openssh git && \
        mkdir /git

WORKDIR /git

VOLUME /root
VOLUME /git

CMD ["git"]

FROM alpine:latest

RUN apk --no-cache add openssh git && \
        mkdir /git && \
        mkdir /home/ety001 && \
        chown -R 1000:1000 /git && \
        chown -R 1000:1000 /home/ety001 && \
        echo "ety001:x:1000:ety001" >> /etc/group && \
        echo "ety001:x:1000:1000:ety001:/home/ety001:/bin/ash" >> /etc/passwd

WORKDIR /git

VOLUME /home/ety001
VOLUME /git

USER ety001

CMD ["git"]

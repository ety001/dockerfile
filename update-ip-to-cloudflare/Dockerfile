FROM alpine:latest as builder
WORKDIR /tmp
RUN apk --no-cache add go git
RUN git clone https://github.com/nickw444/cf-ddns.git && \
    cd cf-ddns && \
    go build -o cf-ddns

FROM alpine:latest
RUN apk --no-cache add curl
COPY --from=builder /tmp/cf-ddns/cf-ddns /usr/bin/
ADD run.sh /usr/bin/run.sh
CMD ["/usr/bin/run.sh"]
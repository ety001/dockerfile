FROM ubuntu:18.04

WORKDIR /data

RUN apt-get update -y && apt-get install -y axel ca-certificates && apt-get clean

ENTRYPOINT ["axel"]
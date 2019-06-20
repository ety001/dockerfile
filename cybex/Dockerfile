FROM ety001/ubuntu-ca:18.04
RUN apt-get update && \
    apt-get install -y libssl1.0.0 \
        libssl-dev \
        libcurl3 \
        libcurl3-gnutls && \
    apt-get clean
WORKDIR /cybex
ADD run.sh /
CMD ["/run.sh"]
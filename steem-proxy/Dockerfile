FROM someguy123/steem:v0.20.2
RUN apt-get update && \
	apt-get install -y proxychains && \
        apt-get clean -qy
COPY proxychains.conf /etc/proxychains.conf
CMD ["sh", "-c", "proxychains /usr/local/bin/steemd"]


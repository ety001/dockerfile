FROM alpine:3.4
RUN apk add --no-cache python3 git gcc alpine-sdk python3-dev libffi-dev \
	openssl-dev openntpd tzdata \
	&& pip3 install pyOpenSSL \
	&& pip3 install git+https://github.com/ety001/python-bts.git \
	&& pip3 install pymongo \
	&& pip3 install pycrypto \
	&& pip3 install graphenelib \
	&& apk del gcc git alpine-sdk python3-dev libffi-dev openssl-dev \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && ntpd -n
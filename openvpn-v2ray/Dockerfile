FROM alpine:3.8
MAINTAINER ety001

WORKDIR /root
ARG TARGETPLATFORM
ARG TAG
COPY v2fly.sh /root/v2fly.sh
COPY v2ray-config.json /tmp/config.json

RUN set -ex \
	&& apk add --no-cache tzdata openssl ca-certificates openvpn \
	&& mkdir -p /etc/v2ray /usr/local/share/v2ray /var/log/v2ray \
    && mv /tmp/config.json /etc/v2ray/config.json \
	&& chmod +x /root/v2fly.sh \
	&& /root/v2fly.sh "${TARGETPLATFORM}" "${TAG}"

CMD [ "/usr/bin/v2ray", "-config", "/etc/v2ray/config.json" ]
ENTRYPOINT ["openvpn"]

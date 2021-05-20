FROM alpine:3.8
MAINTAINER ety001

WORKDIR /root
ARG TARGETPLATFORM
ARG TAG
RUN mkdir -p /etc/supervisor.d/ /etc/v2ray /usr/local/share/v2ray /var/log/v2ray

COPY v2fly.sh /root/v2fly.sh
COPY v2ray-config.json /etc/v2ray/config.json
COPY openvpn.ini /etc/supervisor.d/openvpn.ini
COPY v2ray.ini /etc/supervisor.d/v2ray.ini

RUN set -ex \
	&& apk add --no-cache tzdata openssl ca-certificates openvpn supervisor \
	&& chmod +x /root/v2fly.sh \
	&& /root/v2fly.sh "${TARGETPLATFORM}" "${TAG}"

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]

FROM alpine:3.9
MAINTAINER ety001

WORKDIR /root
ARG TARGETPLATFORM
ARG TAG
RUN mkdir -p /etc/supervisor.d/ /etc/v2ray /usr/local/share/v2ray /var/log/v2ray

COPY v2fly.sh /root/v2fly.sh
COPY v2ray-config.json /etc/v2ray/config.json
COPY openvpn.ini /etc/supervisor.d/openvpn.ini
COPY v2ray.ini /etc/supervisor.d/v2ray.ini
COPY frpc.ini /etc/supervisor.d/frpc.ini

RUN set -ex \
	&& apk add --no-cache tzdata openssl ca-certificates openvpn supervisor \
	&& chmod +x /root/v2fly.sh \
	&& /root/v2fly.sh "${TARGETPLATFORM}" "${TAG}" \
	&& wget https://github.com/fatedier/frp/releases/download/v0.36.2/frp_0.36.2_linux_amd64.tar.gz \
	&& tar zxvf frp_0.36.2_linux_amd64.tar.gz \
	&& mv frp_0.36.2_linux_amd64 /usr/local/bin/frp

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]

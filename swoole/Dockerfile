## Project Page: https://github.com/ety001/docker-swoole
FROM alpine:latest
MAINTAINER ety001 <ety001@domyself.me>
VOLUME /source
RUN apk add --no-cache \
        php7 php7-openssl php7-sqlite3 php7-pear php7-pdo_mysql php7-pcntl \
        php7-common php7-xsl php7-fpm php7-mysqlnd php7-mbstring php7-mysqli \
        php7-xmlreader php7-xmlrpc php7-opcache php7-pdo_sqlite php7-json php7-dev \
    && apk add --no-cache \
        --virtual .build-php-dev autoconf build-base linux-headers \
        libaio-dev openssl \
    && pecl7 install swoole \
    && echo "extension=swoole.so" >> /etc/php7/php.ini \
    && apk del .build-php-dev \
    && ulimit -SHn 65535
COPY ./entry.sh /entry.sh
RUN /bin/chmod u+x /entry.sh
CMD ["/entry.sh"]

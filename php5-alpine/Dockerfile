FROM alpine:3.6
# php
RUN apk --no-cache add php5 php5-pdo_mysql php5-pcntl php5-common \
        php5-xsl php5-fpm php5-mysqli \
        php5-xmlrpc php5-pdo_sqlite \
        php5-sqlite3 php5-exif php5-opcache php5-posix \
        php5-gd php5-gettext php5-json php5-xml php5-iconv php5-curl \
        php5-pdo_pgsql php5-mcrypt php5-dom \
        php5-phar php5-ctype

# composer
ENV COMPOSER_VERSION 1.6.5
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV PATH ${PATH}:/root/.composer/vendor/bin
RUN apk --no-cache add curl && \
        curl -L https://github.com/composer/composer/releases/download/${COMPOSER_VERSION}/composer.phar > /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer

# fix libiconv
RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php

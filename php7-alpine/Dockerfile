FROM alpine:3.6
# php
RUN apk --no-cache add php7 php7-pdo_mysql php7-pcntl php7-common \
        php7-xsl php7-fpm php7-imagick php7-mysqlnd \
        php7-fileinfo php7-mbstring php7-xmlrpc php7-pdo_sqlite \
        php7-sqlite3 php7-exif php7-opcache php7-posix php7-session \
        php7-gd php7-gettext php7-json php7-xml php7-iconv php7-curl \
        php7-pdo_pgsql php7-mcrypt php7-dom php7-memcached \
        php7-simplexml php7-phar php7-ctype php7-tokenizer php7-redis

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

FROM alpine:3.9
# composer
ENV COMPOSER_VERSION 1.8.4
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV PATH ${PATH}:/root/.composer/vendor/bin

# php
RUN apk --no-cache add curl php7 php7-pdo_mysql php7-pcntl php7-common \
  php7-xsl php7-fpm php7-imagick php7-mysqlnd php7-intl php7-bcmath php7-soap \
  php7-fileinfo php7-mbstring php7-xmlrpc php7-pdo_sqlite php7-xmlwriter php7-zip \
  php7-sqlite3 php7-exif php7-opcache php7-posix php7-session php7-zlib \
  php7-gd php7-gettext php7-json php7-xml php7-iconv php7-curl php7-xmlreader \
  php7-pdo_pgsql php7-pgsql php7-mcrypt php7-dom php7-memcached php7-mysqli \
  php7-simplexml php7-phar php7-ctype php7-tokenizer php7-redis && \
  sed -ri 's/^nobody:x:99:20:/nobody:x:65534:65534:/' /etc/passwd && \
  sed -ri 's/nogroup:x:65533:/nogroup:x:65534:/' /etc/group && \
  curl -L https://github.com/composer/composer/releases/download/${COMPOSER_VERSION}/composer.phar > /usr/local/bin/composer && \
  chmod +x /usr/local/bin/composer && \
  apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community gnu-libiconv

ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php
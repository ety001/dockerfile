FROM ubuntu:18.04

COPY sources.list /etc/apt/sources.list
RUN apt-get clean \
        && apt-get -y update \
        && apt-get install -y locales curl \
        && locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php7.2-bcmath php7.2-bz2 \
                php7.2-cli php7.2-common php7.2-curl \
                php7.2-dev php7.2-fpm php7.2-gd php7.2-gmp php7.2-imap php7.2-intl \
                php7.2-json php7.2-ldap php7.2-mbstring php7.2-mysql \
                php7.2-odbc php7.2-opcache php7.2-pgsql php7.2-phpdbg php7.2-pspell \
                php7.2-readline php7.2-recode php7.2-soap php7.2-sqlite3 \
                php7.2-tidy php7.2-xml php7.2-xmlrpc php7.2-xsl php7.2-zip \
                php-mongodb php-tideways

# config
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/cli/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/fpm/php.ini
RUN sed -i "s/display_errors = Off/display_errors = On/" /etc/php/7.2/fpm/php.ini
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/" /etc/php/7.2/fpm/php.ini
RUN sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php/7.2/fpm/php.ini
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.2/fpm/php.ini

RUN sed -i -e "s/pid =.*/pid = \/var\/run\/php7.2-fpm.pid/" /etc/php/7.2/fpm/php-fpm.conf
RUN sed -i -e "s/error_log =.*/error_log = \/proc\/self\/fd\/2/" /etc/php/7.2/fpm/php-fpm.conf
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.2/fpm/php-fpm.conf
RUN sed -i "s/listen = .*/listen = 9000/" /etc/php/7.2/fpm/pool.d/www.conf
RUN sed -i "s/;catch_workers_output = .*/catch_workers_output = yes/" /etc/php/7.2/fpm/pool.d/www.conf

# composer
ENV COMPOSER_VERSION 1.6.5
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV PATH ${PATH}:/root/.composer/vendor/bin
RUN curl -L https://github.com/composer/composer/releases/download/${COMPOSER_VERSION}/composer.phar > /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer

# clear
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 9000
CMD ["php-fpm7.2"]


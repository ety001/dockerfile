FROM alpine:latest
RUN apk --no-cache add php7 php7-curl php7-json
WORKDIR /app
COPY index.php /app/index.php
EXPOSE 80
CMD ["php", "-S", "0.0.0.0:80", "-t", "/app"]
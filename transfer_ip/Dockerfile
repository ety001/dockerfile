FROM alpine:latest
WORKDIR /app
COPY transfer_ip.py .
RUN apk --no-cache add python3 && pip3 install requests
CMD ['python3', '/app/transfer_ip.py']
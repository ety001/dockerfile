FROM alpine:latest
WORKDIR /app
RUN apk --no-cache add python3 && pip3 install requests
COPY transfer_ip.py .
CMD ["/app/transfer_ip.py"]

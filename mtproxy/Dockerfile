FROM alpine:latest
WORKDIR /app
ENV port=6969 secret=e10adc3949ba59abbe56e057f20f883e
RUN apk --no-cache add git nodejs && \
        git clone https://github.com/FreedomPrevails/JSMTProxy.git . && \
        apk del git && \
        sed -i "s/6969/$port/g" /app/config.json && \
        sed -i "s/b0cbcef5a486d9636472ac27f8e11a9d/$secret/g" /app/config.json
CMD ["node", "mtproxy.js"]

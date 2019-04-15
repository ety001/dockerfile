FROM node:alpine
WORKDIR /app
ENV NODE_PATH=/usr/local/lib/node_modules

RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm install -g cordova \
    && apk del .gyp \
    && apk add --no-cache git python2 alpine-sdk

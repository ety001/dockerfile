FROM node:alpine
WORKDIR /app
ENV NODE_PATH=/usr/local/lib/node_modules

RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm install -g --unsafe steem \
    && apk del .gyp

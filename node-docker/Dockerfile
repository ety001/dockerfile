FROM ubuntu:18.04

WORKDIR /app
COPY sources.list /etc/apt/sources.list

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 10.15.3

RUN rm /bin/sh && ln -s /bin/bash /bin/sh &&\
        apt-get update &&\
        apt-get install -y curl &&\
        apt-get -y clean all &&\
        curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash

RUN /bin/bash -c \
        "source $NVM_DIR/nvm.sh \
        && nvm install $NODE_VERSION \
        && nvm alias default $NODE_VERSION \
        && nvm use default"
 
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN npm config set registry https://registry.npm.taobao.org

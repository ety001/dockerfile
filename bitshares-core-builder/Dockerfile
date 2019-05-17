FROM ubuntu:16.04
WORKDIR /app
ARG TAG=master
ARG http_proxy=http://192.168.199.84:8001/
ARG https_proxy=http://192.168.199.84:8001/
RUN apt-get update && apt-get -y install autoconf cmake git libboost-all-dev libssl-dev g++ libcurl4-openssl-dev 
RUN git clone https://github.com/bitshares/bitshares-core.git && cd bitshares-core && git checkout ${TAG} && git submodule update --init --recursive && cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo . && make -j16

FROM ubuntu:16.04
WORKDIR /app/
VOLUME /data_dir
EXPOSE 8090
RUN apt-get update && apt-get -y install libcurl4-openssl-dev && apt-get -y clean
COPY --from=0 /app/bitshares-core/programs/cli_wallet/cli_wallet .
COPY --from=0 /app/bitshares-core/programs/witness_node/witness_node .
CMD ["/app/witness_node", "--data-dir", "/data_dir"]

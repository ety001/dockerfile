FROM ubuntu:16.04 as builder
WORKDIR /app
ARG TAG=master
RUN apt-get update && apt-get -y install autoconf cmake git libboost-all-dev libssl-dev g++ libcurl4-openssl-dev 
RUN git clone https://github.com/bitshares/bitshares-core.git && cd bitshares-core && git checkout ${TAG} && git submodule update --init --recursive && cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo . && make

FROM ubuntu:16.04
WORKDIR /app
VOLUME /data_dir
EXPOSE 8090
COPY --from=builder /app/programs/cli_wallet/cli_wallet /app
COPY --from=builder /app/programs/witness_node/witness_node /app
CMD ["/app/witness_node --data-dir /data_dir"]

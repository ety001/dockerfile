docker run -itd --name bts-core --restart always -v $(pwd)/bts-data:/data_dir --network bts-es_esnet --ip "172.22.0.4" ety001/bts-core:3.3.2 /app/witness_node --data-dir /data_dir --plugins "elasticsearch" --elasticsearch-node-url "http://172.22.0.2:9200/"

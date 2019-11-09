# Docker for Bitshares Elasticsearch

## How to deploy

### 1. Clone the code

```
$ git clone https://github.com/ety001/dockerfile.git
$ cd dockerfile/bts-es
```

### 2. Edit the docker-composer.yaml

> If you want to setup a single node cluster, please use `docker-composer.yaml.single`

* **ES_JAVA_OPTS=-Xms3g -Xmx3g** can edit your elastic memory usage.
* **ELASTIC_PASSWORD** is your elastic password. Please edit `--elasticsearch-basic-auth` at the same time.
* **#ports: - 9200:9200**, if you want to export elastic search http port directly, uncomment this.
* **#ports: - 5601:5601**, if you want to export kibana http port directly, uncomment this.

### 3. Edit password of kibana

Open `kibana.yml` file and edit the `elasticsearch.password` to the elastic search password.

### 4. Create certs

```
$ docker run \
    -it --rm \
    -v $(pwd)/ssl:/usr/share/elasticsearch/config/certs \
    docker.elastic.co/elasticsearch/elasticsearch:7.3.2 \
    /bin/bash

-- GET IN CONTAINER --

# elasticsearch-certutil ca
ENTER ENTER

# elasticsearch-certutil cert --ca elastic-stack-ca.p12
ENTER ENTER ENTER

# mv *.p12 config/certs/
# chown 1000:1000 config/certs/*.p12

# exit
```

### 5. Increase the vm.max_map_count

```
$ sudo sysctl -w vm.max_map_count=262144
```

To set this value permanently, update the `vm.max_map_count` setting  
in `/etc/sysctl.conf`. To verify after rebooting, run `sysctl vm.max_map_count`.

### 6. Edit kibana password

```
$ vim kibana.yml
```
Please change `elasticsearch.password` to your password.

### 7. Run

```
$ docker-compose up -d
```

> If you use single node cluster, please run these commands to close sharp.

```
$ docker exec -it es01 /bin/bash

-- GET IN CONTAINER --

# vi config/elasticsearch.yml

-- Add this config and save --
index.number_of_replicas: 0

# exit
```

## Other Commands

### 1. Check logs

```
$ docker-compose logs -f --tail 100
```

### 2. Stop

```
$ docker-compose down
```

### 3. Check if elastic search is online

```
$ curl -u elastic:123456 -X GET 'http://172.22.0.2:9200/_cat/health'
```
> `123456` is the password which you have set in `docker-compose.yml`.

### 4. Add es01 into nginx network

If you have nginx which deployed by docker, you can add `es01` container  
into nginx network. And then nginx can proxy to `es01`.

> Assume that nginx container network's name is lnmp.
```
docker network connect --ip 172.20.0.3 lnmp es01
```

## Anonymous account

My es node url : [https://bts-es.liuye.tech](https://bts-es.liuye.tech).  
**The anonymous account**  
Username: bts  
Password: btsbts  

## Any question?

Please be easy to commit an issue if you have any question.

My bitshares account: **ety001**  
My witness account: **liuye**

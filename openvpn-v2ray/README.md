# 使用

openvpn登陆文件重命名为 `client.ovpn`

```
docker run -itd --name vpn \
    --restart always \
    --cap-add=NET_ADMIN \
    --device /dev/net/tun \
    -v $(pwd):/root \
    -p 1082:1080 \
    -p 8002:8000 \
    ety001/openvpn-v2ray
```


# 编译命令

```
docker build -t ety001/openvpn-v2ray --build-arg TAG=v4.39.1 .
```

> TAG 是 v2ray 的版本

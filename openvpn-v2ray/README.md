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

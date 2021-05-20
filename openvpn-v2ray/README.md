```
docker run -itd --name vpn \
    --restart always \
    --cap-add=NET_ADMIN \
    --device /dev/net/tun \
    -v $(pwd):/root \
    -p 1082:1080 \
    -p 8002:8000 \
    ety001/openvpn-v2ray \
    --config /root/client.ovpn --auth-nocache
```

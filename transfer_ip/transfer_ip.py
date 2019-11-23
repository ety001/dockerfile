#!/usr/bin/python3
import requests
import json, os, sys, time
from contextlib import suppress
env_dist = os.environ
ip_url = env_dist.get('IP_URL')
to_url = env_dist.get('TO_URL')
if not to_url:
    print('no TO_URL config')
    exit(0)
print(to_url)

def main():
    tmp_ip = ''
    if ip_url:
        url = ip_url
    else:
        url = 'https://ifconfig.me'
    print(url)
    while True:
        try:
            # get ip
            ip_addr = requests.get(url).text.strip()
            print(ip_addr)
            if ip_addr != tmp_ip:
                # send ip
                result = requests.get(to_url+ip_addr, timeout=5).text
                print(result)
                tmp_ip = ip_addr
        except Exception as e:
            print(e)
        time.sleep(10)

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        main()

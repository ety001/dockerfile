#!/usr/bin/python
import requests
import json, os, sys, time
env_dist = os.environ
ip_url = env_dist.get('IP_URL')
to_url = env_dist.get('TO_URL')
if not to_url:
    print('no to_url config')
    exit(0)

def main():
    tmp_ip = ''
    while True:
        # get ip
        if ip_url:
            url = ip_url
        else:
            url = 'https://ifconfig.me'
        ip_addr = requests.get(url).text
        print(ip_addr)
        if ip_addr != tmp_ip:
            # send ip
            result = requests.get(to_url+ip_addr).text
            print(result)
            tmp_ip = ip_addr
        time.sleep(10)

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        main()
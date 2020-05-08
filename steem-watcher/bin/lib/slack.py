#encoding:UTF-8
import json, os, sys, time

env_dist = os.environ
slack_url = env_dist.get('SLACK_URL')

def send(msg):
    if slack_url == None:
        print("\n-------Has not config SLACK_URL.-------\n")
        return
#!/bin/ash
FILE=/tmp/ip.txt
while :
do
    echo "start"
    lastip=""
    if [ -f $FILE ]; then
        lastip=`cat $FILE`
    fi
    nowip=`curl -s ifconfig.so`
    if [[ "$lastip" == "$nowip" ]]; then
        echo "not need update
    else
        cf-ddns \
            --cf-email=$CF_EMAIL \
            --cf-api-key=$CF_KEY \
            --cf-zone-id=$CF_ZONEID \
            --ip-address=$nowip \
            $DOMAIN
        echo "$nowip" > /tmp/ip.txt
        echo "ip updated"
    fi
    sleep $SLEEP_TIME
done
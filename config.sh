#!/bin/bash
STATUS=""
while [ "$STATUS" != "200" ]
do
    sleep 1
    STATUS=$(curl -sL -w "%{http_code}" http://web -o /dev/null)
done
python3 opt/data/filldata.py http://web 
echo "config ok"
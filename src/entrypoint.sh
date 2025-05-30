#!bin/sh

ping -c 1 172.16.238.10
ping -c 1 172.16.238.20
ping -c 1 172.16.238.30
tail -f /dev/null
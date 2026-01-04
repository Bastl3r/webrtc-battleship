#!/bin/sh
export EXTERNAL_IP=$(curl -s ifconfig.me)
exec turnserver -c /etc/coturn/turnserver.conf
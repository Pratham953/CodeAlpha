#!/bin/bash

ATTACKER_IP=$1
LOG_FILE="blocked_ips.log"

if [ -z "$ATTACKER_IP" ]; then
    echo "No IP provided"
    exit 1
fi

# Block attacker IP
sudo iptables -A INPUT -s $ATTACKER_IP -j DROP

# Log the action
echo "$(date) - Blocked IP: $ATTACKER_IP" >> $LOG_FILE

echo "Blocked attacker IP: $ATTACKER_IP"

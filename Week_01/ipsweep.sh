#!/bin/bash

# this is for-loop: for something(ip= ip here is just a variable, we cann declare it something else if we want like i ) in something(seq 1 254= from 1 to 254 these are the last part of the ip address for example for the first time the first ip address will be pinged(192.168.1.(1)), for the last time the last ip address will be 192.168.1.(255) accourding to the seq in the loop ) do the command.
# $1 = user input(the argument in this case is the first three octets of the ip address, the $ip is the sequence(the forth octet of the ip address).
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"
else
for ip in `seq 1 254` ; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done 
fi
#./ipsweep.sh 192.168.1

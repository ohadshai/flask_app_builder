#!/bin/bash

bold='\033[1m'
red='\e[31m'
green='\e[32m'
yel='\e[33m'
blu='\e[34m'
mag='\e[35m'
cyn='\e[36m'
end='\e[0m'

crossmark="${red}\u2718${end}"
checkmark="${green}\u2714${end}"

print_info(){
    	msg=$1
    	echo -e "${bold}${msg}${end}"
}

failure(){
	msg=$1
    	echo -e "${crossmark} ${red}${msg}${end}"
    	exit -1
}

success(){
    	msg=$1
    	echo -e "${checkmark} ${green}${msg}${end}"
}

success_bold(){
    	msg=$1
    	echo -e "${bold}${green}${msg}${end}"
}

check_root(){
   	if [[ $EUID -ne 0 ]]; then
      		failure "This script must be run as root"
	fi
}

check_linux(){
	os=$(uname -s)
	if [ $os != "Linux" ]; then 
		failure "This script can run only on Linux system"
	fi 	
}

check_connection(){
	curl -s  http://google.com > /dev/null
	if [ $? -eq 0 ]; then
		success "Connected to Network"		
	else
    failure "Connection to network failed. Check connection..."
fi
}


check_root
check_linux
check_connection
# System Dependencies
yum update -y
yum install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv

# Python Dependencies
python3 -m virtualenv venv
. venv/bin/activate

pip3 install -r requirements.txt

cp bidera.service /etc/systemd/system/

systemctl start bidera

#gunicorn --bind 0.0.0.0:5000 wsgi:app

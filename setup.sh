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


print_pink(){
    msg=$1
    echo -e "${bold}${cyn}${msg}${end}"
}

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

check_exit_code(){
  exit_code=$?
  err_msg=$1
  success_msg=$2
  if [[ $exit_code -ne 0 ]]; then
    failure "$err_msg"
  elif [[ ! -z $success_msg ]]; then
    success "$success_msg"
  fi
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

host_info(){
  host_info=$(hostnamectl)
  print_info "-------------------    Host Info    ------------------------"
  print_pink "$host_info"
  print_info "------------------------------------------------------------"
  print_info "Starting Installation..."
}

check_connection(){
	curl -s  http://google.com > /dev/null
	check_exit_code "Connection to network failed. Check connection..." "Connected to Network"
}

install_yum_packages(){
  print_info "Updating yum.."
  yum update -y > /dev/null
  check_exit_code "yum update failed" "yum update finished successfully"
  print_info "Install yum packages"
  yum -y groupinstall "Development Tools"
  yum -y install openssl-devel bzip2-devel libffi-devel wget
}

install_python3(){
  print_info "Installing Python3.8"
  mkdir downloads
  wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz -P downloads
  tar xvf downloads/Python-3.8.7.tgz -C downloads
  pushd downloads/Python-3.8.7 > /dev/null
  ./configure --enable-optimizations
  make altinstall
  popd > /dev/null
  ln -s /usr/local/bin/python3.8 /usr/local/bin/python3
  ln -s /usr/local/bin/pip3.8 /usr/local/bin/pip3
  sed -i -e '/secure_path/ s[=.*[&:/usr/local/bin[' /etc/sudoers
  ## ERROR HERE. doesn't reload changes in sudoers
  python3 --version
  check_exit_code "python3 failed to install" "python3 installed successfully"
  pip3 --version
  check_exit_code "pip3 failed to install" "pip3 installed successfully"
  pip3 install virtualenv
  check_exit_code "virtualenv failed to install" "virtualenv installed successfully"
}

create_virtualenv(){
  python3 -m virtualenv venv
  . venv/bin/activate
  pip3 install -r requirements.txt
}



main(){
  check_root
  check_linux
  host_info
  check_connection
  install_yum_packages
  install_python3
  create_virtualenv

  cp bidera.service /etc/systemd/system/
  print_info "starting Bidera Service"
  systemctl start bidera
}
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

#gunicorn --bind 0.0.0.0:5000 wsgi:app

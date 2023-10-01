#!/bin/bash

# MySQL Server Installation, Configuration, and Startup
#--------------------------------------------------------------------------
DATA_DIRECTORY="var/lib/mysql"
MYSQL_ROOT_PASSWORD="Root12345!"
MYSQL_API_PASSWORD="Api12345!"

echo "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD" | sudo debconf-set-selections
echo "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD" | sudo debconf-set-selections

# install MySQL Server
sudo apt-get update
sudo apt-get install -y mysql-server
# start MySQL Server
sudo systemctl start mysql

# create MySQL database
sql_execute() {
	local input="$1"
	echo "$input" | sudo mysql -u root -p$MYSQL_ROOT_PASSWORD
}
sql_execute "CREATE DATABASE authentication;"
sql_execute "INSTALL PLUGIN validate_password SONAME 'validate_password.so';"
sql_execute "CREATE USER 'api'@'localhost' IDENTIFIED BY '$MYSQL_API_PASSWORD'"
sql_execute "FLUSH PRIVILEGES;"


# Python Virtual Enviroment Setup and Server Startup
#--------------------------------------------------------------------------
cd ./backend
echo "After cd $(pwd)"
sudo apt update
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate
pip install --no-input -r requirements.txt

# add uvicorn script to the PATH
if ! which uvicorn >/dev/null 2>&1; then
	UVICORN_PATH=$(pip show uvicorn | grep Location | awk '{print $2}')
	echo $UVICORN_PATH
	export PATH="$UVICORN_PATH:$PATH"
fi
# start uvicorn server in a separate process
uvicorn app:app &

# JS Environment and Server Startup
#--------------------------------------------------------------------------
cd ../frontend
sudo apt-get install -y nodejs npm
npm ci
npm run dev &


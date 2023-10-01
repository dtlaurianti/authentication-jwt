#!/bin/bash
# deactivate python venv
#------------------------------------------------------------------------------
deactivate
# kill and uninstall MySQL
#------------------------------------------------------------------------------
sudo mysqladmin -uroot shutdown
sudo killall -KILL mysql mysqld_safe mysqld
sudo apt remove mysql-client-8.0 mysql-client-core-8.0 mysql-common mysql-server mysql-server-8.0 mysql-server-core-8.0 -y
sudo apt purge mysql-client-8.0 mysql-client-core-8.0 mysql-common mysql-server mysql-server-8.0 mysql-server-core-8.0 -y
sudo rm -rf /var/lib/mysql /etc/mysql*
sudo rm -rf /etc/apparmor.d/abstractions/mysql /etc/apparmor.d/cache/usr.sbin.mysqld /etc/mysql /var/lib/mysql /var/log/mysql* /var/log/upstart/mysql.log* /var/run/mysqld
sudo deluser --remove-home mysql
sudo delgroup mysql
sudo apt-get autoremove -y
sudo apt-get autoclean -y

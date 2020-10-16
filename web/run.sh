#!/bin/sh
if [ ! -f /etc/phpmyadmin/config.secret.inc.php ] ; then
    cat > /etc/phpmyadmin/config.secret.inc.php <<EOT
<?php
\$cfg['blowfish_secret'] = '$(tr -dc 'a-zA-Z0-9~!@#$%^&*_()+}{?></";.,[]=-' < /dev/urandom | fold -w 32 | head -n 1)';
EOT
fi

if [ ! -f /etc/phpmyadmin/config.user.inc.php ] ; then
  touch /etc/phpmyadmin/config.user.inc.php
fi

mkdir -p /var/nginx/client_body_temp
chown nobody:nobody /sessions /var/nginx/client_body_temp
mkdir -p /var/run/php/
chown nobody:nobody /var/run/php/
touch /var/log/php-fpm.log
chown nobody:nobody /var/log/php-fpm.log
echo "http://mirrors.aliyun.com/alpine/latest-stable/main/" > /etc/apk/repositories
echo "http://mirrors.aliyun.com/alpine/latest-stable/community/" >> /etc/apk/repositories
# 同步时间
 
# 更新源、安装openssh 并修改配置文件和生成key 并且同步时间
sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config 
ssh-keygen -t dsa -P "" -f /etc/ssh/ssh_host_dsa_key 
ssh-keygen -t rsa -P "" -f /etc/ssh/ssh_host_rsa_key 
ssh-keygen -t ecdsa -P "" -f /etc/ssh/ssh_host_ecdsa_key 
ssh-keygen -t ed25519 -P "" -f /etc/ssh/ssh_host_ed25519_key 
echo "root:admin" | chpasswd

/usr/sbin/sshd
if [ "$1" = 'phpmyadmin' ]; then
    exec supervisord --nodaemon --configuration="/etc/supervisord.conf" --loglevel=info
fi

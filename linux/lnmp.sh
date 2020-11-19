#!/bin/bash
#author:aikeke
nginx_tar=nginx-1.8.0.tar.gz
yum_ok(){
num=`yum repolist|awk -F: '/repolist/{print $2}'|sed 's/,//'`
if [ $num -lt 100 ];then
        echo "please check yum is ok?"
        exit 1
fi
}

menu(){
clear
echo "  #########---Menu---########"
echo " # 1. Install Nginx"
echo " # 2. Install MySQL"
echo " # 3. Install PHP"
echo " # 4. EXIT"
echo "  ###########################"
}

choice(){
read -p "please choice a menu[1-9]:" select
}

Install_Nginx(){
id nginx&>/dev/null
if [ $? -ne 0 ];then
        sudo useradd -s /sbin/nologin nginx
fi
if [ -f $nginx_tar ];then
        tar -xf $nginx_tar
        cd ${nginx_tar%.tar*}
        yum install -y gcc pcre zlib-devel pcre-devel openssl-devel  make $>/dev/null
        ./configure --prefix=/usr/local/nginx --with-http_ssl_module
        make & make install
        if [ $? -eq 0 ];then
                echo "nginx 安装成功"
        fi
        ln -s /usr/local/nginx/sbin/nginx /usr/sbin/
else
        echo "没有nginx源码包"
fi
}

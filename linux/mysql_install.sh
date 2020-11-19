!/bin/bash
#date:20190514
#author:ayf
#执行脚本前请先下载安装包到脚本所在目录
#下载地址：https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.26-linux-glibc2.12-x86_64.tar.gz
#该脚本执行时间较长，请耐心等待，不要中断该脚本，或者可以放入后台执行
basedir=/usr/local/
datadir=/data/mysql/
useradd -s /sbin/nologin mysql
mkdir -p $datadir
chown -R mysql:mysql $datadir

#卸载mysql旧版，如果之前有源码安装的mysql，请手动删除
rpm -qa |egrep -i "mariadb|mysql"|xargs rpm -e --nodeps

tar -xzf mysql-5.7.26-linux-glibc2.12-x86_64.tar.gz
mv mysql-5.7.26-linux-glibc2.12-x86_64 $basedir
mv ${basedir}mysql-5.7.26-linux-glibc2.12-x86_64 ${basedir}mysql

#配置my.cnf
cat >/etc/my.cnf <<EOF
[mysql]
# CLIENT #
port                           = 3306
socket                         = ${datadir}mysql.sock
default-character-set=utf8mb4

[mysqld]
# GENERAL #
user                           = mysql
default-storage-engine         = InnoDB
socket                         = ${datadir}mysql.sock
pid-file                       = ${datadir}mysql.pid
server_id                      = 12

# SAFETY #
max-allowed-packet             = 16M
max-connect-errors             = 1000000
skip-name-resolve
sql-mode                       = STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_AUTO_VALUE_ON_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY
sysdate-is-now                 = 1
innodb                         = FORCE

# DATA STORAGE #
datadir                        = ${datadir}

# BINARY LOGGING #
log-bin                        = ${datadir}mysql-bin
expire-logs-days               = 14
sync-binlog                    = 1
binlog_format                  = ROW

# CACHES AND LIMITS #
tmp-table-size                 = 32M
max-heap-table-size            = 32M
query-cache-type               = 0
query-cache-size               = 0
max-connections                = 500
thread-cache-size              = 50
open-files-limit               = 65535
table-definition-cache         = 1024
table-open-cache               = 2048
# INNODB #
innodb-flush-method            = O_DIRECT
innodb-log-files-in-group      = 2
innodb-log-file-size           = 512M
innodb-flush-log-at-trx-commit = 1
innodb-file-per-table          = 1
innodb-buffer-pool-size        = 26G

# LOGGING #
log-error                      = ${datadir}mysql-error.log
log-queries-not-using-indexes  = 1
slow-query-log                 = 1
slow-query-log-file            = ${datadir}mysql-slow.log

# OTHERS #
lower_case_table_names         = 1
transaction-isolation          = REPEATABLE-READ
character-set-client-handshake = FALSE
character-set-server           = utf8mb4
collation-server               = utf8mb4_unicode_ci
init_connect                   = 'SET NAMES utf8mb4'
sql_mode                       = NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
EOF

#数据库初始化
${basedir}mysql/bin/mysqld --initialize --user=mysql --basedir=${basedir}mysql --datadir=$datadir

#配置环境变量
echo "export PATH=${basedir}mysql/bin:\$PATH" >>/etc/profile
source /etc/profile

#配置服务启动
cp ${basedir}mysql/support-files/mysql.server /etc/init.d/
cd /etc/init.d
mv mysql.server mysql
sed -i "46s?basedir=?basedir=${basedir}mysql?g" mysql
sed -i "47s?datadir=?datadir=$datadir?g" mysql

#启动并检查mysql
/etc/init.d/mysql start


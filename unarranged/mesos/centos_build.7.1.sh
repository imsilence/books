#!/bin/sh

yum install -y wget

wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo


yum groupinstall -y "Development Tools"echo [WANdiscoSVN] > /etc/yum.repos.d/wandisco-svn.repo
echo name=WANdisco SVN Repo 1.9 >> /etc/yum.repos.d/wandisco-svn.repo
echo enabled=1 >> /etc/yum.repos.d/wandisco-svn.repo
echo baseurl=http://opensource.wandisco.com/centos/7/svn-1.9/RPMS/x86_64/ >> /etc/yum.repos.d/wandisco-svn.repo
echo gpgcheck=1 >> /etc/yum.repos.d/wandisco-svn.repo
echo gpgkey=http://opensource.wandisco.com/RPM-GPG-KEY-WANdisco >> /etc/yum.repos.d/wandisco-svn.repo


yum install -y apache-maven python-devel java-1.7.0-openjdk-devel zlib-devel libcurl-devel openssl-devel cyrus-sasl-devel cyrus-sasl-md5 apr-devel subversion-devel apr-util-devel

g++ --version
#!/bin/sh

yum install -y tar wget which

wget -O /etc/yum.repos.d/slc6-devtoolset.repo http://linuxsoft.cern.ch/cern/devtoolset/slc6-devtoolset.repo

rpm --import http://linuxsoft.cern.ch/cern/centos/7/os/x86_64/RPM-GPG-KEY-cern

wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo

echo [WANdiscoSVN] > /etc/yum.repos.d/wandisco-svn.repo
echo name=WANdisco SVN Repo 1.8 >> /etc/yum.repos.d/wandisco-svn.repo
echo enabled=1 >> /etc/yum.repos.d/wandisco-svn.repo
echo baseurl=http://opensource.wandisco.com/centos/6/svn-1.8/RPMS/i686/ >> /etc/yum.repos.d/wandisco-svn.repo
echo gpgcheck=1 >> /etc/yum.repos.d/wandisco-svn.repo
echo gpgkey=http://opensource.wandisco.com/RPM-GPG-KEY-WANdisco >> /etc/yum.repos.d/wandisco-svn.repo

yum groupinstall -y "Development Tools"

yum install -y devtoolset-2-toolchain

yum install -y apache-maven python-devel java-1.7.0-openjdk-devel zlib-devel libcurl-devel openssl-devel cyrus-sasl-devel cyrus-sasl-md5 apr-devel subversion-devel apr-util-devel

scl enable devtoolset-2 bash

g++ --version
#ssh 密钥登录#

1. 生成公私钥
ssh-keygen -t rsa -b 4096 -C "kk"

2. 在登录主机中加入公钥
echo id_rsa_4096.pub >> ~/.ssh/authorized_keys

3. 修改authorized_keys权限
chmod 700 ~/.ssh/
chmod 600 ~/.ssh/authorized_keys

4. 打开
启动key认证
配置文件/etc/ssh/sshd_config
修改:
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile      .ssh/authorized_keys

关闭密码认证
PasswordAuthentication no

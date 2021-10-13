# 基础环境搭建--Python3安装

> Auth: 王海飞
>
> Data：2021-10-13
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge



# Centos7安装Python3.7

全部操作都在`root`用户下执行

## 1.安装编译相关工具

```shell
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum install libffi-devel -y
```

## 2.下载安装包解压

```shell
cd #回到用户目录
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar -xvJf  Python-3.7.0.tar.xz
```

## 3.编译安装

```shell
mkdir /usr/local/python3 #创建编译安装目录
cd Python-3.7.0
./configure --prefix=/usr/local/python3
make && make install
```

## 4.创建软连接

```shell
ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3
```

## 5.验证是否成功

```shell
python3 -V
pip3 -V
```
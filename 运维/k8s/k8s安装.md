

# Kubernetes使用指南--入门基础

> Auth: 王海飞
>
> Data：2020-08-06
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge

------

### 前言

​	kubernetes，简称K8s，是一个开源的，用于管理云平台中多个主机上的容器化的应用，Kubernetes的目标是让部署容器化的应用简单并且高效（powerful）,Kubernetes提供了应用部署，规划，更新，维护的一种机制。

#### 1. 部署方式

k8s的部署方式：

    kubesadmin（初学使用）
    
    二进制（开发环境用得多）
    
    minikube（测试环境，快速的启动）
    
    yum

#### 2. 安装

需要安装以下内容：

    docker / kubeadm / kubelet / kubectl

##### 2.1 安装kubeadm

默认情况下安装kubernetes需要google外网。可以通过设置以下的镜像站来绕过google：

```haskell
google地址被墙的情况下可以使用阿里云或者中科大的镜像站：

sudo apt-get update && sudo apt-get install -y apt-transport-https curl

sudo curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -

# 向源文件kubernetes.list中加入源
sudo tee /etc/apt/sources.list.d/kubernetes.list <<-'EOF'
deb https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial main
EOF

# 更新源
sudo apt-get update

# 安装kubeadm (只需安装kubeadm就可以将kubectl喝kubelet一起安装好了)
apt install kubeadm
```



# DOCKER使用指南

> Auth: 王海飞
>
> Data：2019-04-28
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge
>
>

------

## 前言

​        docker hub是一个docker容器管理平台，其完全可以满足我们对镜像管理的需求，而且使用也非常方便，但是上传的镜像任何人都可以访问，其次docker hub的私有仓库又是收费的，所以从安全和商业两方面考虑，企业必须搭建自己的私有镜像仓库。

 	官方的Docker Hub registry用于储存Docker镜像，因此本文将介绍如何配置一个私有的Docker registry，在此上传的镜像是私密的，我们可以从另一个联网的主机以安全的方式下载此私有docker仓库中的镜像。

### 1. 私有docker仓库的搭建

搭建docker私有仓库服务器，再该私有仓库服务器上运行registry容器并管理镜像。操作如下：

#### 1)  拉取registry镜像，命令为：docker pull registry

![图](images/1pull_registry.png)

#### 2）基于registry镜像运行名为registry_new容器

![图](images/2run_contains.png)

**参数说明**
-itd：在容器中打开一个伪终端进行交互操作，并在后台运行；
-v：把宿主机的/data/registry目录绑定 到 容器/var/lib/registry目录(这个目录是registry容器中存放镜像文件的目录)，来实现数据的持久化；
-p：映射端口；访问宿主机的5000端口就访问到registry容器的服务了；
--restart=always：这是重启的策略，假如这个容器异常退出会自动重启容器；
--name registry_new：创建容器命名为registry_new；
registry:latest：这个是刚才pull下来的镜像；

#### 3）测试镜像仓库中是否有上传的镜像

![图](images/3.curl_regitries.png)

**注意:** 初始化私有仓库中镜像为空，当上传了镜像后，则镜像仓库中将出现上传的镜像。如上图所示，busybox就为上传到私有仓库的镜像。

### 2. 镜像的拉取与使用
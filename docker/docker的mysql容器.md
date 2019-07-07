# DOCKER使用指南

> Auth: 王海飞
>
> Data：2019-06-28
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge
>
> 

------

## 前言

​        docker hub是一个docker容器管理平台，其完全可以满足我们对镜像管理的需求，而且使用也非常方便，但是上传的镜像任何人都可以访问，其中有很多基础镜像，如mysql、mongo等

### 1. MySQL容器的搭建

操作如下：

#### 1)  拉取mysql镜像，命令为：docker pull mysql

```
# 拉取基础镜像mysql
docker pull myqsl
```

#### 2）基于mysql镜像运行容器

```
# 基于基础镜像mysql创建容器
 docker run -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d docker.io/mysql:latest
```

**参数说明**
-e：设置环境变量；如设置数据库密码的三个参数为: MYSQL_ROOT_PASSWORD、MYSQL_ALLOW_EMPTY_PASSWORD 、MYSQL_RANDOM_ROOT_PASSWORD 
-p：映射端口；如将宿主机的3306端口映射到容器中的3306端口上。
-d：后台运行，镜像docker.io/mysql:latest所创建的容器。

-it：交互式运行。

### 2. 遇到问题 

#### 1）如果在可视化工具中连接Mysql报错, ‘*Client* *does* *not* *support* *authentication* protocol requested by server ’ 。解决办法如下
```
# 使用mysql数据库
use mysql;

# 修改protocol模式
alter user 'root'@'localhost' identified with mysql_native_password by '密码';

# 刷新权限
flush privileges;
```



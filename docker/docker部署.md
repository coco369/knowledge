# DOCKER使用指南--部署

> Auth: 王海飞
>
> Data：2019-05-01
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge
>
>

***

### 1.Dockerfile文件定义

```
FROM 47.240.0.28:5000/lesoubase:v1

MAINTAINER wanghaifei

ADD ./answer_django /home/src/answer_django
WORKDIR /home/src/answer_django


ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8099"]
```

![图](images/docker_bushu_build.png)

### 2.start.sh文件定义

```
#!/usr/bin/env bash

echo "***************************** Step 1 ***************************************"

echo "Build new container"
docker build -t lesou:v1 .

echo "***************************** Step 2 ***************************************"
echo "Start new container"
docker run --restart="always" -d -p 9090:8099 \
    -e 'LANG=zh_CN.UTF-8' \
    -e 'LANGUAGE=zh_CN.UTF-8' \
    -e 'LC_ALL=zh_CN.UTF-8' \
    --name lesou \
    lesou:v1
echo ""
```

![图](images/docker_bushu_run.png)
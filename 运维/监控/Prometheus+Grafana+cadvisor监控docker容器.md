## 监控Docker容器各项指标

### 前言

​		需求：能够实现 可视化监控、告警提醒、日志收集等功能。

​		解决方案：Grafana做可视化、Prometheus做日志收集、Cadvisor做Docker相关指标采集

### 1. Docker性能指标
#### 1.1） 查看容器ID 2181e3276b60 的相关指标

    查看容器CPU的使用情况
    docker stats --no-stream 2181e3276b60 | awk '{print $3}'

说明：cadvisor可以用于 收集容器资源使用的相关信息

### 2.Prometheus的部署

普罗米修斯容器：
```
docker run -itd -p 9090:9090 -v /tmp/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml  prom/prometheus
```
编辑/tmp/prometheus/prometheus.yml文件
```
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]
  
  - job_name: "docker"

    static_configs:
      - targets: ["172.17.0.1:8080"]
```

说明：

​	1） job_name是任务名称

​	2）static_configs 的 targets是监听的服务地址

注意:  prometheus.yml中监听了两个任务，分别是9090的peometheus服务 以及 8080的cadvisor服务

### 3. cadvisor的部署

​		Google的 cAdvisor 是另一个知名的开源容器监控工具。

​		只需在宿主机上部署cAdvisor容器，用户就可通过Web界面或REST服务访问当前节点和容器的性能数据(CPU、内存、网络、磁盘、文件系统等等)，非常详细。
​		默认cAdvisor是将数据缓存在内存中，数据展示能力有限；它也提供不同的持久化存储后端支持，可以将监控数据保存、汇总到Google BigQuery、InfluxDB或者Redis之上。

docker启动命令：


```
docker run --volume=/:/rootfs:ro --volume=/var/run:/var/run:rw --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --volume=/dev/disk/:/dev/disk:ro --publish=8080:8080 --detach=true --name=cadvisor unibaktr/cadvisor
```

### 4. grafana的部署

​		Grafana是运维数据可视化平台，能提供丰富的数据看板，让运维监控更加高效、精细。

docker启动命令：

```
docker run -itd -p 3000:3000 grafana/grafana
```

默认账号密码为：admin/admin


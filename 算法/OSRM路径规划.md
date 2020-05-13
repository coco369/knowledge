## 前言

用C ++ 14编写的高性能路由引擎，旨在在OpenStreetMap数据上运行。

通过HTTP API，C ++库接口和NodeJs包装器可以使用以下服务：

- 最近-将坐标捕捉到街道网络并返回最近的匹配项
- 路线-查找坐标之间的最快路线
- 表格-计算所有提供的坐标对之间最快路线的持续时间或距离
- 匹配-以最合理的方式将嘈杂的GPS轨迹捕捉到道路网络
- 旅行-使用贪婪启发式方法解决旅行商问题
- 切片-生成具有内部路由元数据的Mapbox矢量切片

##### 1. 安装OSRM

> 安装相关依赖
```
1.1 安装cmake工具，用于编译c相关文件
brew install cmake

1.2 安装gcc
brew install gcc
```
> 从github上获得源代码

git clone https://github.com/Project-OSRM/osrm-backend.git

> 进入下拉的osrm-backend文件夹，并编译

```bash
mkdir -p build

cd build

cmake ..

cmake --build .

sudo cmake --build . --target install
```



##### 2. 下载地图文件

OSRM依赖OpenStreetMap的数据。可以在 [http://download.geofabrik.de](http://download.geofabrik.de/) 下载。选择pbf即可。示例：

```
`wget http:``//download``.geofabrik.de``/europe/germany/berlin-latest``.osm.pbf`
```

##### 3. 初始化地图


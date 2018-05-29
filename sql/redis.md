
# redis使用指南

>Auth: 王海飞
>Data：2018-04-18
>Email：779598160@qq.com
>github：https://github.com/coco369/knowledge

#### 背景

```
redis和mysql要根据具体业务场景去选型
    
mysql：数据放在磁盘   redis：数据放在内存
redis适合放一些频繁使用，比较热的数据，因为是放在内存中，读写速度都非常快
 
首先要知道mysql存储在磁盘里，redis存储在内存里，redis既可以用来做持久存储，也可以做缓存，而目前大多数公司的存储都是mysql + redis，其中：
mysql作为主存储，redis作为辅助存储被用作缓存，加快访问读取的速度，提高性能。
 
那么为什么不直接全部用redis存储呢？
因为redis存储在内存中，如果存储在内存中，存储容量肯定要比磁盘少很多，那么要存储大量数据，只能花更多的钱去购买内存，造成在一些不需要高性能的地方是相对比较浪费的，所以目前基本都是mysql(主) + redis(辅)，在需要性能的地方使用redis，在不需要高性能的地方使用mysql，好钢用在刀刃上
1）mysql支持sql查询，可以实现一些关联的查询以及统计；
2）redis对内存要求比较高，在有限的条件下不能把所有数据都放在redis；
3）mysql偏向于存数据，redis偏向于快速取数据，但redis查询复杂的表关系时不如mysql，所以可以把热门的数据放redis，mysql存基本数据

```

#### 1.安装

##### a) centos7中安装redis
  1.由于CentOS官方yum源里面没有Redis,这里我们需要安装一个第三方的yum源,这里用了Fedora的epel仓库
    ```
      yum install epel-release
    ```
  安装过程中一直输入y按回车就可以了

  2.安装redis
    ```
      yum install redis
    ```
    同样也是一直输入y按回车就可以了

  3.启动redis
   ```
    service redis start
   ```
  如果输入提示 Redirecting to /bin/systemctl start  redis.service这个语句，则直接输入/bin/systemctl start  redis.service去启动redis

  4. 查看redis的状态
   ```
   service redis status
   或者
   /bin/systemctl status  redis.service
  ```
  
  5.重启redis
  ```
    service redis restart
    或者
    /bin/systemctl restart  redis.service
  ```
  
  6. 关闭redis
  ```
   service redis stop
    或者
   /bin/systemctl stop  redis.service
  ```
##### b) 测试
 PING
     使用客户端向 Redis 服务器发送一个 PING ，如果服务器运作正常的话，会返回一个 PONG 。通常用于测试与服务器的连接是否仍然生效，或者用于测量延迟值。
 返回值：
     如果连接正常就返回一个 PONG ，否则返回一个连接错误。


#### 2.修改 redis.conf文件

##### a) 配置文件
  配置文件位置：redisd 配置信息在 /etc/redis.conf中

##### b) 修改登录密码
 在vim中通过搜索:/requirepass 可以找到如下配置
  ```
   #requirepass foobared

  如果取消该注释，修改foobared的值新的密码值，并保存文件，则说明redis重启以后需要输入新设置的密码newfoobared登录

   requirepass newfoobared
  ```
  然后重启

##### c) 进入redis
    直接使用redis-cli命令进入，使用auth 加密码进行验证
    如果auth密码验证失败的话提示 (error) NOAUTH Authentication required. 错误
    
##### d) 退出
    quit： 关闭连接（connection）
    
    
#### 3.五中主要的类型和命令

redis是键值对的数据库，有5中主要数据类型：

字符串类型（string），散列类型（hash），列表类型（list），集合类型（set），有序集合类型（zset）

 

几个基本的命令：

KEYS * 获得当前数据库的所有键

EXISTS key [key ...]  判断键是否存在，返回个数，如果key有一样的也是叠加数

DEL key [key ...]       删除键，返回删除的个数

TYPE key                  获取减值的数据类型（string，hash，list，set，zset）

FLUSHALL                清空所有数据库

CONFIG [get、set]    redis配置

 

-inf 负无穷

+inf正无穷


###### a）字符串类型string

```
字符串类型是Redis的最基本类型，它可以存储任何形式的字符串。其它的四种类型都是字符串类型的不同形式。

最基本的命令：GET、SET         语法：GET key，SET key value   value如果有空格需要双引号以示区分

整数递增：INCR                      语法：INCR key    默认值为0，所以首先执行命令得到 1 ，不是整型提示错误

增加指定的整数：INCRBY          语法：INCRBY key increment

整数递减：DECR                     语法：DECR key   默认值为0，所以首先执行命令得到 -1，不是整型提示错误

减少指定的整数：DECRBY         语法：DECRBY key increment

增加指定浮点数：INCRBYFLOAT 语法：INCRBYFLOAT key increment  与INCR命令类似，只不过可以递增一个双精度浮点数

向尾部追加值：APPEND             语法：APPEND key value   redis客户端并不是输出追加后的字符串，而是输出字符串总长度

获取字符串长度：STRLEN          语法：STRLEN key  如果键不存在返回0，注意如果有中文时，一个中文长度是3，redis是使用UTF-8编码中文的

获取多个键值：MGET                语法：MGET key [key ...]  例如：MGET key1 key2 

设置多个键值：MSET                语法：MSET key value [key value ...]  例如：MSET key1 1 key2 "hello redis"

二进制指定位置值：GETBIT        语法：GETBIT key offset   例如：GETBIT key1 2 ，key1为hello 返回 1，返回的值只有0或1，

　　　　　　　　　　　　　　　　　　 当key不存在或超出实际长度时为0

设置二进制位置值：SETBIT       语法：SETBIT key offset value ，返回该位置的旧值

二进制是1的个数：BITCOUNT    语法：BITCOUNT key [start end] ，start 、end为开始和结束字节

位运算：BITOP                       语法：BITOP operation destkey key [key ...]  ，operation支持AND、OR、XOR、NOT

偏移：BITPOS                        语法：BITPOS key bit [start] [end]

 ```
 

###### b) 散列类型hash

 ```
设置单个：HSET                      语法：HSET key field value，不存在时返回1，存在时返回0，没有更新和插入之分

设置多个：HMSET                    语法：HMSET key field value [field value ...]

读取单个：HGET                      语法：HGET key field，不存在是返回nil

读取多个：HMGET                    语法：HMGET key field [field ...]

读取全部：HGETALL                 语法：HGETALL key，返回时字段和字段值的列表

判断字段是否存在：HEXISTS      语法：HEXISTS key field，存在返回1 ，不存在返回0

字段不存在时赋值：HSETNX       语法：HSETNX key field value，与hset命令不同，hsetnx是键不存在时设置值

增加数字：HINCRBY                 语法：HINCRBY key field increment ，返回增加后的数，不是整数时会提示错误

删除字段：HDEL                      语法：HDEL key field [field ...] ，返回被删除字段的个数

只获取字段名：HKEYS               语法：HKEYS key ，返回键的所有字段名

只获取字段值：HVALS              语法：HVALS key  ，返回键的所有字段值

字段数量：HLEN                      语法：HLEN key ，返回字段总数

```

###### c) 列表类型（list）

```
内部使用双向链表实现，所以获取越接近两端的元素速度越快，但通过索引访问时会比较慢

添加左边元素：LPUSH               语法：LPUSH key value [value ...]  ，返回添加后的列表元素的总个数

添加右边元素：RPUSH              语法：RPUSH key value [value ...]  ，返回添加后的列表元素的总个数

移除左边第一个元素：LPOP        语法：LPOP key  ，返回被移除的元素值

移除右边第一个元素：RPOP        语法：RPOP key ，返回被移除的元素值 

列表元素个数：LLEN                语法：LLEN key， 不存在时返回0，redis是直接读取现成的值，并不是统计个数

获取列表片段：LRANGE           语法：LRANGE key start stop，如果start比stop靠后时返回空列表，0 -1 返回整个列表

                                                    正数时：start 开始索引值，stop结束索引值（索引从0开始）

                                                    负数时：例如 lrange num -2 -1，-2表示最右边第二个，-1表示最右边第一个，

删除指定值：LREM                  语法：LREM key count value，返回被删除的个数

                                                   count>0，从左边开始删除前count个值为value的元素

                                                   count<0，从右边开始删除前|count|个值为value的元素

                                                   count=0，删除所有值为value的元素

索引元素值：LINDEX               语法：LINDEX key index ，返回索引的元素值，-1表示从最右边的第一位

设置元素值：LSET                  语法：LSET key index value

保留列表片段：LTRIM              语法：LTRIM key start stop，start、top 参考lrange命令

一个列表转移另一个列表：RPOPLPUSH      语法：RPOPLPUSH source desctination ，从source列表转移到desctination列表，

                                                                 该命令分两步看，首先source列表RPOP右移除，再desctination列表LPUSH

 
```

###### d) 集合类型（set）

```
集合类型值具有唯一性，常用操作是向集合添加、删除、判断某个值是否存在，集合内部是使用值为空的散列表实现的。

添加元素：SADD                    语法：SADD key member [member ...] ，向一个集合添加一个或多个元素，因为集合的唯一性，所以添加相同值时会被忽略。

　　　　　　　　　　　　　　　         返回成功添加元素的数量。

删除元素：SREM                    语法：SREM key member [member ...] 删除集合中一个或多个元素，返回成功删除的个数。

获取全部元素：SMEMBERS      语法：SMEMBERS key ，返回集合全部元素

值是否存在：SISMEMBER        语法：SISMEMBER key member ，如果存在返回1，不存在返回0

差运算：SDIFF                      语法：SDIFF key [key ...] ，例如：集合A和集合B，差集表示A-B，在A里有的元素B里没有，返回差集合；多个集合(A-B)-C

交运算：SINTER             　　 语法：SINTER key [key ...]，返回交集集合，每个集合都有的元素

并运算：SUNION　　　　　　  语法：SUNION key [key ...]，返回并集集合，所有集合的元素

集合元素个数：SCARD           语法：SCARD key ，返回集合元素个数

集合运算后存储结果                语法：SDIFFSTROE destination key [key ...] ，差运算并存储到destination新集合中

　　　　　　　　　　 　　　　　　　 SINTERSTROE destination key [key ...]，交运算并存储到destination新集合中

                                                  SUNIONSTROE destination key [key ...]，并运算并存储到destination新集合中

随机获取元素：SRANDMEMGER 语法：SRANDMEMBER key [count]，根据count不同有不同结果，count大于元素总数时返回全部元素

　　　　　　　　　　　　　　　　　　count>0 ，返回集合中count不重复的元素

　　　　　　　　　　　　　　　　　　count<0，返回集合中count的绝对值个元素，但元素可能会重复

弹出元素：SPOP                     语法：SPOP key [count] ，因为集合是无序的，所以spop会随机弹出一个元素

```

###### e) 有序集合类型

```
添加集合元素：ZADD              语法：ZADD key [NX|XX] [CH] [INCR] score member [score member ...]，不存在添加，存在更新。

获取元素分数：ZSCORE          语法：ZSCORE key member ，返回元素成员的score 分数

元素小到大：ZRANGE             语法：ZRANGE key start top [WITHSCORES] ，参考LRANGE ，加上withscores 返回带元素，即元素，分数

                                                  当分数一样时，按元素排序

元素大到小：ZREVRANGE       语法：ZREVRANGE key start [WITHSCORES] ，与zrange区别在于zrevrange是从大到小排序

指定分数范围元素：ZRANGEBYSCORE   语法：ZRANGEBYSCORE key min max [WITHSCORE] [LIMIT offest count]

 　　　　　　　　　　　　　　　返回从小到大的在min和max之间的元素，( 符号表示不包含，例如：80-100，(80 100，

　　　　　　　　　　　　　　    withscore返回带分数

　　　　　　　　　　　　　　    limit offest count 向左偏移offest个元素，并获取前count个元素

指定分数范围元素：ZREVRANGESCORE   语法：ZREVRANGEBYSCORE key max  min [WITHSCORE] [LIMIT offest count]

　　　　　　　　　　　　　　　 与zrangebyscore类似，只不过该命令是从大到小排序的。

增加分数：ZINCRBY                语法：ZINCRBY key increment member ，注意是增加分数，返回增加后的分数；如果成员不存在，则添加一个为0的成员。

```

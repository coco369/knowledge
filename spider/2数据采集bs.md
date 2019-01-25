
# 爬虫学习使用指南

>Auth: 王海飞
>
>Data：2018-06-15
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 前言

数据采集，针对网页获取源码，按照一定的正则匹配，或者xpath的规则去匹配出我们需要的结果，进行分类筛选入库等操作。在本章中会讲到beautifulsoup工具去爬取网页，获取相关需要的信息。


### 1. BeautifSoup

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.-----引入[官网地址](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)的一句话

#### 1.1 安装与导入

Beautiful Soup 4 通过PyPi发布,所以如果你无法使用系统包管理安装,那么也可以通过 easy_install 或 pip 来安装.包的名字是 beautifulsoup4 ,这个包兼容Python2和Python3.

	pip install beautifulsoup4

导入方式: 

	from bs4 import beautifulsoup4

解析器类型:

	Python 标准库 BeautifulSoup(html, “html.parser”) 速度⼀般，容错能⼒好
	lxml HTML解析器 BeautifulSoup(html, “lxml”) 速度快，容错好
	lxml xml解析器 BeautifulSoup(markup, “xml”) 速度快，唯⼀⽀持xml
	html5lib BeautifulSoup(markup, “html5lib”) 容错性⾼，速度慢

解析器的安装:

	# 安装解析器
	　　pip install lxml
	
	# 另一个可供选择的解析器是纯Python实现的 html5lib，html5lib的解析方式与浏览器相同
		pip install html5lib

#### 1.2 解析语法

##### <b style="color:red;"> 标准选择器</b>

find_all( name , attrs , recursive , text , **kwargs )

find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

	查询所有a标签的内容
	soup.find_all('a')
	
	查询所有a标签下class样式为bb的内容
	soup.find_all('a', 'bb')

	查询所有id样式为cc的内容
	soup.find_all(id='cc')

##### <b style="color:red;"> 标签选择器</b>

通过标签名字选择，选择速度快，如果存在多个相同的标签则只返回第一个。

	# head标签里面title的文字内容
	print(soup.title)
	print(soup.title.string)
	print(soup.head.title.string)

	# 取整个head标签的内容
	print(soup.head)
	print(type(soup.head))

	# 获取第一个p标签的内容	
	print(soup.p)
	# 获取第一个p标签的名称
	print(soup.p.name)
	# 获取第一个p标签下的第一个a标签的标签名称
	print(soup.p.a.name)
	# 获取第一个p标签中的内容
	print(soup.p.contents)
	
	# 获取第一个img标签的所有属性	
	print(soup.img.attrs)
	# 获取第一个img标签属性中的src属性
	print(soup.img.attrs["src"])
	print(soup.img['src'])


###### <b style="color:red;"> 类/CSS选择器</b>
 	
	# 获取class="news-list-b"标签中class="list"的标签下的class="item"下的p标签中的a标签内容
	result = soup.select('.news-list-b .list .item p a')
	for item in result:
		print(item.string)
	
	# 获取class中定义的两个样式参数
	result = soup.select('.-live-layout-row.layout_sports_350_650')
	print(result)
	
	# 获取class="title"的标签下的a标签内容
	l = soup.select('.ct_t_01 a')
	for item in l:
		print(item.string)
	 	print(item['href'])
	print(len(l))
	
	# 获取属性
	print(soup.select('#list-2 h1')[0].attrs)
	
	# 获取内容
	print(soup.select('#list-2 h1')[0].get_text())


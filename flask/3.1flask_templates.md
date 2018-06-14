

# flask使用操作指南之模板

>Auth: 王海飞
>
>Data：2018-05-15
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 1. jinja2

Flask中使用jinja2模板引擎

jinja2是由Flask作者开发，模仿Django的模板引擎

优点：
	
	速度快，被广泛使用

	HTML设计和后端python分离

	非常灵活，快速和安全

	提供了控制，继承等高级功能


### 2. 模板语法


#### 2.1 模板语法主要分为两种：变量和标签

模板中的变量：{{ var }}

	视图传递给模板的数据

	前面定义出来的数据

	变量不存在，默认忽略

模板中的标签：{% tag %}
	
	控制逻辑

	使用外部表达式

	创建变量

	宏定义

#### 2.2 结构标签：

block
	
	{% block xxx %}

	{% endblock %}

	块操作
		父模板挖坑，子模板填坑

extends
	
	{% extends ‘xxx.html’ %}
	
	继承以后保留块中的内容
	{{ super() }}

挖坑继承体现的化整为零的操作


macro
	
	{% macro hello(name) %}

		{{ name }}

	{% endmacro %}
	
	宏定义，可以在模板中定义函数，在其他地方调用

宏定义可导入

	{% from 'xxx' import xxx %}

例子1：

在index.html中定义macro标签，定义一个方法，然后去调用方法，结果是展示商品的id和商品名称

	
	{% macro show_goods(id, name) %}
	    商品id：{{ id }}
	    商品名称：{{ name }}
	{% endmacro %}
	
	{{ show_goods('1', '娃哈哈') }}
	<br>
	{{ show_goods('2', '雪碧') }}

例子2：

在index.html页面中定义一个say()方法，然后解析该方法：

	{% macro say() %}
	
	    <h3>今天天气气温回升</h3>
	    <h3>适合去游泳</h3>
	    <h3>适合去郊游</h3>
	
	{% endmacro %}
	
	{{ say() }}


例子3：

定义一个function.html中定义一个方法：

	{% macro create_user(name) %}
	    创建了一个用户:{{ name }}
	{% endmacro %}

在index.html中引入function.html中定义的方法

	
	{% from 'functions.html' import create_user %}
	
	{{ create_user('小花') }}



#### 2.3 循环

	{% for item in cols %}

		aa
	
	{% else %}

		bb
	
	{% endfor %}

也可以获取循环信息loop

	loop.first

	loop.last

	loop.index

	loop.revindex

例子:

在视图中定义一个视图函数：

	@stu.route('/scores/')
	def scores():
	
	    scores_list = [21,34,32,67,89,43,22,13]
	
	    content_h2 = '<h2>今天你们真帅</h2>'
	    content_h3 = '   <h3>今天你们真帅</h3>   '
	
	    return render_template('scores.html',
	                           scores=scores_list,
	                           content_h2=content_h2,
	                           content_h3=content_h3)

(该视图函数，在下面讲解的过滤器中任然使用其返回的content_h2等参数)

首先: 在页面中进行解析scores的列表。题目要求：第一个成绩展示为红色，最后一个成绩展示为绿色，其他的不变

   	<ul>
	   {% for score in scores %}
	        {% if loop.first %}
	            <li style="color:red;">{{ loop.revindex }}:{{ loop.index }}:{{ score }}</li>
	        {% elif loop.last %}
	            <li style="color:green;">{{ loop.revindex }}:{{ loop.index }}:{{ score }}</li>
	        {% else %}
	            <li> {{ loop.revindex }}:{{ loop.index }}:{{ score }}</li>
	        {% endif %}
	    {% endfor %}
	</ul>

#### 2.4 过滤器

语法：
	
	{{ 变量|过滤器|过滤器... }}


capitalize 单词首字母大写

lower 单词变为小写

upper 单词变为大写

title

trim 去掉字符串的前后的空格

reverse 单词反转

format

striptags 渲染之前，将值中标签去掉

safe 讲样式渲染到页面中

default

last 最后一个字母

first

length

sum

sort

例子：

	<ul>
	    <li>{{ content_h2 }}</li>
	    <li>{{ content_h2|safe }}</li>
	    <li>{{ content_h2|striptags }}</li>
	
	    <li>{{ content_h3 }}</li>
	    <li>{{ content_h3|length }}</li>
	    <li>{{ content_h3|trim|safe }}</li>
	    <li>{{ content_h3|trim|length }}</li>
	</ul>


### 3. 定义模板

#### 3.1 定义基础模板base.html

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>
	        {% block title %}
	        {% endblock %}
	    </title>
	    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
	
	    {% block extCSS %}
	    {% endblock %}
	</head>
	<body>

	{% block header %}
	{% endblock %}
	
	{% block content%}
	{% endblock %}
	
	{% block footer%}
	{% endblock %}
	
	{% block extJS %}
	{% endblock %}

	</body>
	</html>


#### 3.2 定义基础模板base_main.html


	{% extends 'base.html' %}
	
	{% block extCSS %}
	    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
	{% endblock %}

### 4. 静态文件信息配置

<b>django</b>：

第一种方式：

	{% load static %}
	<link rel="stylesheet" href="{% static 'css/index.css' %}">

第二种方式：

	<link rel="stylesheet" href="/static/css/index.css">


<b>flask</b>：

第一种方式：

	<link rel="stylesheet" href="/static/css/index.css">

第二种方式：

	<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">

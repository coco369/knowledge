
# tornado使用操作指南--模板与静态资源

>Auth: 王海飞
>
>Data：2019-02-17
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 


### 1. 模板

在Web开发阶段中为了提高模板的灵活性和重用性，通常使用模板继承。在Tornado中可以通过使用extends和block语句块来定义模板继承。Tornado的模板继承方式和Django框架或Flask框架的模板继承有异曲同工之处，如实先创建一个基本的‘骨架’父模板，在父模板中定义block语句，而子模板只需继承父模板，并重写对应的block语句即可。

语法格式:

<b> 1）block块定义 </b>
	
	{% block name %} {% end %}

<b> 2）继承 </b>

	{% extends ‘父模板页面’ %}

<b> 3) 模板渲染 </b>
	
	self.render('temp.html', items=items)，其中items为向模板temp.html中传递的参数

### 2. 模板继承

定义index.html页面，并使用继承的形式继承父模板base.html页面

<b> 1）父模板base.html</b>

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>
	        {% block title %}
	        {% end %}
	    </title>
	
	    {% block css %}
	    {% end %}
	
	    {% block js %}
	    {% end %}
	</head>
	<body>
	    {% block header %}
	    {% end %}
	
	    {% block content %}
	    {% end %}
	</body>
	</html>

父模板base.html只用定义网站的大体结构并定义可以被子模板重写的block块标签即可。而子模板只需继承base.html页面，并自定义父模板base.html中的block。

<b> 2）定义继承于base.html的子模板index.html</b>
	
	<!--继承父模板base.html-->
	{% extends 'base.html' %}
	
	<!--重写名为content的block块内容-->
	{% block content %}
	    <p>加载模板页面</p>
	{% end %}


注意: index.html模板在修改为继承之前和之后的效果没变化。只是使用继承的形式来修改模板以后，可以给开发带来很大的灵活性，大大提高模板的维护性。

### 3. 模板语法

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tornado的模板语法在一定程度上和Django的模板语法，以及和Flask的模板语法都是非常的相似。模板中可以使用Python表达式和控制语句进行标记，动态的打印信息。在模板中填充Python变量的值，可以使用双大括号来渲染。而在模板中使用Python表达式和循环语句，则需要使用{% 表达式 %}语法。

<b style="color:red;"> 语法格式: </b>

<b> 1）解析标签 </b>

{% 标签 %} {% end %}，标签有if、for、while、try、set等

<b> 2）解析变量 </b>

{{ 变量 }}

<b> 3）注解 </b>

{# 注解内容 #}、{% comment 注解内容 %}，这两种方式都可以注解内容，且注解的内容在页面源码中不会出现。

#### 3.1 标签

<b> 1) for标签 </b>

	语法格式: {% for a in  b %} 内容体 {% end %}

渲染temp.html页面，并动态刷新传递给页面的参数:

	class TempHandler(tornado.web.RequestHandler):
	
	    def get(self):
	        items = ['Python', 'Html', 'Django', 'Flask', 'Tornado']
	        self.render('temp.html', items=items)
	
	
	def make_app():
	    return tornado.web.Application(
	        handlers=[
	            (r"/temp/", TempHandler),
	        ],
	        template_path=os.path.join(os.path.dirname(__file__), "templates")
	    )


使用self.render()方法渲染temp.html页面，并绑定需在页面中解析的参数items。

temp.html模板页面代码:

	<!--继承父模板base.html-->
	{% extends 'base.html' %}
	
	<!--重写名为content的block块内容-->
	{% block content %}
	    {% for i in items %}
	        <p>{{ i }}</p>
	    {% end %}
	{% end %}

<b> 2) if标签 </b>

在temp.html页面中判断循环的items参数，如果当前for循环解析的变量为‘Python’，  则添加展示的样式，将变量修改为红色。判断条件可以使用if标签，具体语法如下:

<b>{% if 判断条件 %} 内容体 {% end %}

{% if 判断条件 %} 内容体 {% else %}内容体{% end %}

{% if 判断条件 %} 内容体 {% elif 判断条件 %}内容体{% else %}内容体{% end %}</b>


修改temp.html页面代码，使用if标签判断执行条件:
	
	<!--继承父模板base.html-->
	{% extends 'base.html' %}
	
	<!--复写名为content的block块内容-->
	{% block content %}
	    长度为: {{ len(items) }}
	    <br>
	    第一个元素为: {{ items[0] }}
	    <br>
	    遍历items中每一个元素：
	    {% for i in items %}
	        {% if i == 'Python' %}
	            <p style="color:red;">{{ i }}</p>
	        {% elif i == 'Flask' %}
	            <p style="color:yellow;">{{ i }}</p>
	        {% else %}
	            <p>{{ i }}</p>
	        {% end %}
	    {% end %}
	    <!--while循环-->
	{% end %}

注意: 在示例模板中解析items参数，可以使用Python中语法解析，如len(items)计算items变量的长度，items[0]通过小标取出items列表中的第一个元素等。

<b> 3) while标签 </b>

在模板中还可以使用while循环判断，使用语法和Python中语法一样。while循环中还可以使用{% break %}和{% continue %}进行跳出循环的操作。

while循环语法格式: 

<b>{% while 循环条件 %} 内容体 {% end %} </b>

修改temp.html页面代码，使用while循环依次打印items变量中的每一个元素。

	<!--继承父模板base.html-->
	{% extends 'base.html' %}
	
	<!--复写名为content的block块内容-->
	{% block content %}
	    <!--while循环-->
	    while循环前items中元素为: {{ items }}
	    <br>
	    {% while len(items) %}
	        {{ items.pop() }}
	        <br>
	    {% end %}
	    while循环后items中元素为: {{ items }}
	{% end %}


<b> 4) set标签 </b>

在模板中可以设置局部变量，语法格式如下:

<b>{% set a=b %}，设置局部变量a，且a的值为b </b>

修改temp.html页面代码，设置变量n并赋值为1。

	<!--继承父模板base.html-->
	{% extends 'base.html' %}
	
	<!--复写名为content的block块内容-->
	{% block content %}
	    <!--set赋值-->
	    {% set n = 1 %}
	    {{ n }}
	{% end %}

<b> 5) try标签 </b>

模板中可以定义异常处理try来捕获异常，并做对应的处理。模板中的异常处理try语法和Python中的try异常捕获语法是一致的。

语法格式如下:

<b>{% try %} 内容体 {% except %} 内容体 {% else %} 内容体 {% finally %}内容体{% end %}</b>

修改temp.html页面代码，使用try异常捕获错误，并做相关处理。

	<!--继承父模板base.html-->
	{% extends 'base.html' %}
	
	<!--复写名为content的block块内容-->
	{% block content %}
	    <!--try-->
	    {{ items }}
	    {% try %}
	        {{ items[10] }}
	    {% except %}
	        <p>items列表取元素异常</p>
	    {% else %}
	        <p>items取值结束</p>
	    {% finally %}
	        <p>finally必须执行</p>
	    {% end %}
	{% end %}

### 4. 静态文件配置与加载

在Web开发中，层叠样式的使得页面变得炫丽多彩，其中层叠样式的加载也可以通过外链的形式进行导入。<b style="color:red;">在Tornado项目中可以向Appication类的构造函数中传递一个static_path参数，用以告诉Tornado从static_path指定的路径去加载静态文件。</b>

配置静态static_path路径。如下:

	def make_app():
	    return tornado.web.Application(
	        handlers=[
	            (r"/", IndexHandler),
	            (r"/temp/", TempHandler),
	        ],
	        template_path=os.path.join(os.path.dirname(__file__), "templates"),
	        static_path=os.path.join(os.path.dirname(__file__), 'static')
	    )

通过设置static_path路径为当前应用目录下的static子目录作为静态文件，在模板中即可通过Tornado模板<b style="color:red;">提供的static_url函数</b>来生成static目录下文件的URL地址，如下示例定义页面中如何加载静态文件（默认在static文件夹下一个style.css文件）。

修改index.html页面代码，并加载static文件夹下的样式style.css文件。

	<!--继承父模板base.html-->
	{% extends 'base.html' %}
	
	{% block css %}
	    <!--第一种加载方式: 硬编码-->
	    <link rel="stylesheet" href="/static/style.css">
	
	    <!--第二种加载方式: 使用static_url-->
	    <link rel="stylesheet" href="{{ static_url('style.css') }}">
	
	{% end %}
	
	<!--重写名为content的block块内容-->
	{% block content %}
	    <p>加载模板页面</p>
	{% end %}

示例中分别通过两种方式来加载层叠样式style.css文件:<b style="color:red;"> 硬编码和static_url</b>。注意使用这两种方式来加载样式，其最终的效果是一样的，但是也有所区别，区别如下:

1）<b>硬编码:</b> 引入固定的style.css文件地址。写法固定但如果改变静态文件目录，由static修改为static_file，则需要将每一个页面中引用静态资源文件的硬编码地址都修改一遍。

2) <b>使用static_url生成静态URL地址:</b> 通过源码可以发现调用static_url生成静态文件的URL地址为: <link rel="stylesheet" href="/static/style.css?v=fff729bfd91bc81011839847c8b509f0">，从解析的href地址中可以发现在URL地址后生成了一个参数v。参数v是static_url函数创建了一个基于文件内容的hash值，这个hash值确保了浏览器总是加载这个style.css的最新版，而不是加载缓存中的style.css文件。

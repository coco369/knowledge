

# flask使用操作指南之表单验证

>Auth: 王海飞
>
>Data：2018-09-11
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 前言

在Flask项目开发中针对提交表单的校验，可以使用Flask-WTF扩展库进行快速的字段校验，也可以进行页面快速渲染，并提供跨站请求伪造的保护功能。

### 1. 安装Flask-WTF

	pip install flask-wtf

### 2. 实现注册功能

#### 2.1 注册表单模型定义

在定义的表单类中定义需要验证的username、password和password2字段，并实现如下校验:

1. 校验密码password2和password相等
2. 校验用户名是否存在
3. 校验用户名的长度是否符合规范

		# 导入扩展类
		from flask_wtf import FlaskForm
		# 导入验证字段
		from wtforms import StringField, SubmitField, ValidationError
		# 导入表单验证
		from wtforms.validators import DataRequired, EqualTo
		
		from user.models import User
		
		
		class UserForm(FlaskForm):
		    """
		    登录注册表单验证
		    """
		    username = StringField('用户名', validators=[DataRequired()])
		    password = StringField('密码', validators=[DataRequired()])
		    password2 = StringField('确认密码', validators=[DataRequired(),
		                                                EqualTo('password', '密码不一致')]
		                            )
		    submit = SubmitField('提交')
		
		    def validate_username(self, field):
		        # 验证用户名是否重复
		        if User.query.filter(User.username == field.data).first():
		            raise ValidationError('用户名已存在')
		
		        # 对用户名的长度进行判断
		        if len(field.data) < 3:
		            raise ValidationError('用户名长度不能少于3个字符')
		
		        if len(field.data) > 6:
		            raise ValidationError('用户名长度不能大于6个字符')
	

<b style='color:red;'>注意: 验证字段的方法名为: validate_字段(self, field)</b>


#### 2.2 定义注册视图函数

当HTTP请求为GET时，将表单验证对象返回给页面。

当HTTP请求为POST时，通过方法validate_on_submit()方法进行字段校验和提交判断，如果校验失败，则可以从form.errors中获取错误信息。

如果验证通过，则从form.字段.data中获取到字段的值。

	@blue.route('/register/', methods=['GET', 'POST'])
	def register():
	    form = UserForm()
	    if request.method == 'GET':
	        return render_template('register.html', form=form)
	
	    if request.method == 'POST':
	        # 判断表单中的数据是否通过验证
	        if form.validate_on_submit():
	            # 获取验证通过后的数据
	            username = form.username.data
	            password = form.password.data
	            # 保存
	            user = User()
	            user.username = username
	            user.password = generate_password_hash(password)
	            user.save()
	            return redirect(url_for('user.login'))
	        return render_template('register.html', form=form)

#### 2.3 模板展示

注册模板采用继承父模板base.html的形式。在register.html模压中分析如下:
	
	1. 定义字段名: {{ form.字段.label }}
	
	2. 定义input输入框: {{ form.字段 }}
	
	3. 展示错误信息: {{ form.errors.字段 }}
	
	4. 跨站请求伪造: {{ form.csrf_token }}

注册register.html页面如下:

	{% extends 'base.html' %}
	
	{% block title %}
	    注册页面
	{% endblock %}
	
	{% block content %}
	    <form action="" method="post">
	        {{ form.csrf_token }}
	        {{ form.username.label }}:{{ form.username(style='color:red;', placeholder='请输入用户名', onblur="alert('123')") }}
	        {{ form.password.label }}:{{ form.password }}
	        {{ form.password2.label }}:{{ form.password2 }}
	        {{ form.submit }}
	
	        {% if form.errors %}
	            姓名错误信息:{{ form.errors.username }}
	            密码错误信息:{{ form.errors.password2 }}
	        {% endif %}
	    </form>
	{% endblock %}

注意: 通过form.字段解析的input标签中可以自定义样式，如{{ form.字段(class='xxx'， style='color:red') }}


### 3. 常见字段类型

	字段类型	说明
	StringField	普通文本字段
	PasswordField	密码文本字段
	SubmitField	提交按钮
	HiddenField	隐藏文本字段
	TextAreaField	多行文本字段
	DateField	文本字段，datetime.date格式
	DateTimeField	文本字段，datetime.datetime格式
	IntegerField	文本字段，整数类型
	FloatField	文本字段，小数类型
	BooleanField	复选框，值为True或False
	RadioField	单选框
	SelectField	下拉列表
	FileField	文件上传字段

### 4. 验证器
	
	验证器	说明
	DataRequired	确保字段有值(并且if判断为真)
	Email	邮箱地址
	IPAddress	IPv4的IP地址
	Length	规定字符长度
	NumberRange	输入数值的范围
	EqualTo	验证两个字段的一致性
	URL	有效的URL
	Regexp	正则验证
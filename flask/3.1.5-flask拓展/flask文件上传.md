

# flask使用操作指南之文件上传

>Auth: 王海飞
>
>Data：2018-10-12
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge


### 前言

文件的上传是Web开发中最常见的功能，如何实现文件的上传，可以使用Flask-Uplaods扩展库实现，也可以使用flask默认的保存文件的方法来实现。 本案例使用flask默认功能来实现文件的上传。


### 1. 模板定义

form表单中定义上传文件的字段，定义type='file'。注意上传的表单中一定要添加enctype="multipart/form-data"参数。

	<form action="" method="post" enctype="multipart/form-data">
        头像:<input type="file" name="icons">
        <input type="submit" value="提交">
    </form>

### 2. 图片保存

图片的保存可以直接通过request.files获取模板中上传的图片，并调用save()方法进行保存。

	# 获取图片
    icons = request.files.get('icons')
    # 保存save(path)
    file_path = os.path.join(UPLOAD_DIR, icons.filename)
    icons.save(file_path)

### 3. 图片渲染

案例的场景是修改当前登录系统用户的icons字段，在模板中可以通过current_user参数获取当前登录系统的用户对象，并访问icons属性即可获取到存储在数据库中的图片路径。

	<img src="/static/media/{{ current_user.icons }}">
	

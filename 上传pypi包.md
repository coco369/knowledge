# 上传自定义的Python包到pypi

> Auth: 王海飞
>
> Data：2020-09-08
>
> QQ群：223058292
>
> WX：wanghaifeige
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/docker-depth-learning
>
> 知乎Docker专栏：<https://zhuanlan.zhihu.com/c_1285288092883734528>
>
> 知乎Python入门专栏：<https://zhuanlan.zhihu.com/c_1277570999509757952>>

### 前言

​	在开发中很多项目都需要使用到共同的功能，如果每个服务都把这个库放置于各自的目录下，维护起来很麻烦，因此把这个公共功能上传到PyPI，通过pip来统一管理。

#### 目录结构

首先将项目的目录组织成如下形式

```text
<my_project>/                 # 项目根目录
|-- <my_package>              # package
|   |-- __init__.py
|   `-- <files> ....          # 代码模块
|-- README.md
|-- LICENSE
|-- setup.py
```

#### 编写setup.py

```
from setuptools import setup, find_packages

setup(
    name="python-aliyun-api-gateway",
    packages=find_packages(),
    version='0.0.1',
    description="aliyun api gateway",
    author="wanghaifei",
    author_email='779598160@qq.com',
    url="https://github.com/coco369/aliyun-api-gateway-python",
    download_url='https://github.com/coco369/aliyun-api-gateway-python',
    keywords=['command', 'line', 'tool'],
    classifiers=[],
    entry_points={
        'console_scripts': [

        ]
    },
    install_requires=[
        'python3.7.6',
    ]
)
```

这里setuptools.setup() 的几个参数的含义如下：

- name - 项目的名称
- version - 项目的版本。需要注意的是，PyPI上只允许一个版本存在，如果后续代码有了任何更改，再次上传需要增加版本号
- author和author_email - 项目作者的名字和邮件
- description - 项目的简短描述
- long_description - 项目的详细描述，会显示在PyPI的项目描述页面。上面的例子里直接用了README.md中的内容做详细描述
- long_description_content_type - 用于指定long_description的markup类型，上面的例子是markdown
- url - 项目主页的URL，一般给出代码仓库的链接
- packages - 指定最终发布的包中要包含的packages。上面的例子中find_packages() 会自动发现项目根目录下所有的packages，当然也可以手动指定package的名字
- install_requires - 项目依赖哪些库，这些库会在pip install的时候自动安装
- entry_points - 上面的例子中entry_points用来自动创建脚本，上面的例子在pip install安装成功后会创建douyin_image这个命令，直接可以在命令行运行，很方便
- classifiers - 其他信息，一般包括项目支持的Python版本，License，支持的操作系统。上面的例子中，我们指定项目只能在Python 3上运行，使用MIT License，不依赖操作系统。关于classifiers的完整列表，可参考 [https://pypi.org/classifiers/](https://link.zhihu.com/?target=https%3A//pypi.org/classifiers/)。

好了项目的文件编辑好了，接下来我们就可以开始打包我们的项目了。

## 上传项目到PyPI

我们使用twine上传项目，先安装twine

```
pip install twine
```

执行一下命令，将在项目目录下生成dist文件夹，

```
python setup.py sdist ``-``-``formats``=``gztar register upload
```


执行完之后，运行下面的命令将库上传

```bash
twine upload dist/*
```

上传完成后，我们的项目就成功地发布到PyPI了。
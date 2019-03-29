
# debug调试使用指南

>Auth: 王海飞
>
>Data：2018-09-17
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge
>

### 前言

在开发中经常要查看方法中所使用的SQL语句，查看开发中各种各样的参数，比如session，cookie和执行的SQL,以及SQL所消耗的时间等等功能。

#### 1. debug-toolbar的安装

安装：

	pip install django-debug-toolbar

#### 2. debug-toolbar的配置

关于debug-toolbar的配置需要在settings.py中添加相关的配置信息。

##### 添加调试工具的IP

	INTERNAL_IPS = ("127.0.0.1",)

##### 添加调试工具中间件
	
	MIDDLEWARE = [
	    ....
	    'debug_toolbar.middleware.DebugToolbarMiddleware', # 添加debug中间件
	]

##### 添加调试工具App
	
	INSTALLED_APPS = [
	    ....
	    'debug_toolbar.apps.DebugToolbarConfig',
	]


##### debug_toolbar 组件选项，默认值为如下12个组件，可根据需要自行调整。此处不写代表使用默认值。

	DEBUG_TOOLBAR_PANELS = [
	    'debug_toolbar.panels.versions.VersionsPanel',
	    'debug_toolbar.panels.timer.TimerPanel',
	    'debug_toolbar.panels.settings.SettingsPanel',
	    'debug_toolbar.panels.headers.HeadersPanel',
	    'debug_toolbar.panels.request.RequestPanel',
	    'debug_toolbar.panels.sql.SQLPanel',
	    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
	    'debug_toolbar.panels.templates.TemplatesPanel',
	    'debug_toolbar.panels.cache.CachePanel',
	    'debug_toolbar.panels.signals.SignalsPanel',
	    'debug_toolbar.panels.logging.LoggingPanel',
	    'debug_toolbar.panels.redirects.RedirectsPanel',
	]


在工程目录的urls.py中添加如下代码：

	if settings.DEBUG:
	    import debug_toolbar
	    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))



# vue使用操作指南--vue路由组件

>Auth: 王海飞
>
>Data：2019-02-22
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 1. 路由基本概念

路由中有三个基本的概念: route, routes, router

<b> 1）route </b>: 指一条路由。

<b> 2）routes </b>: 指一组路由，将route定义的每一条路由组合起来，形成一个数组。

<b> 3）router </b>: 是一个机制，相当于一个管理者，用于管理路由。由于routes只是定义了一组路由，而router用于管理路由。当请求来了，router这是将发挥作用，其回去routes中查找定义的route路由，如果找到定义的路由，则调用相关的组件，返回对应的内容。

### 2. 路由配置

<b>vue-router中的路由也是基于route、routes、route来实现的</b>

　　在vue中实现路由还是相对简单的。因为我们页面中所有内容都是组件化的，我们只要把路径和组件对应起来就可以了，然后在页面中把组件渲染出来。

　　1）页面实现（html模版中）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在vue-router中, 我们看到它定义了两个标签<b><router-link> 和<router-view></b>来对应点击和显示部分。
       
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<router-link> 就是定义页面中点击的部分，<router-view> 定义显示部分，就是点击后，区配的内容显示在什么地方。所以 <router-link> 还有一个非常重要的属性 to，定义点击之后，要到哪里去， 如：<router-link  to="/home">Home</router-link>

　　2）main.js 中配置路由概念

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;首先要定义route,  一条路由的实现。它是一个对象，由两个部分组成： path和component.  path 指路径，component 指的是组件。如：{path:’/home’, component: home}

　　3) 配置，组成一个routes: 

	var routes = [
	  { path: '/home', component: Home },
	  { path: '/about', component: About }
	]
		
   4）创建router 对路由进行管理，它是由构造函数 new vueRouter() 创建，接受routes 参数。
	
	var router = new VueRouter({
	      routes // routes: routes 的简写
	})

　　5）配置完成后，把router 实例注入到 vue 根实例中,就可以使用路由了

	var app = new Vue({
	  router
	}).$mount('#app')

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行过程：当用户点击 router-link 标签时，会去寻找它的 to 属性， 它的 to 属性和 js 中配置的路径{ path: '/home', component: Home}  path 一一对应，从而找到了匹配的组件， 最后把组件渲染到 <router-view> 标签所在的地方。

# vue使用操作指南--vue内部指令

>Auth: 王海飞
>
>Data：2019-02-21
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge


### 1. 指令

Vue的内部指令: 

1)：指令是带有v-前缀的特殊特性，值限定为绑定表达式，也就是js表达式以及过滤器

2)：指令的作用是当表达式的值发生变化的时候，将这个变化也反应到DOM上。
   比如: <div v-if="show">DDFE</div>  当show为true的时候，展示DDFE字样，否则不展示

3)：有一些指令的语法有些不一样，在指令与表达式之间插入一个参数，用冒号分隔，如v-bind指令<a v-bind:href="url"></a>或者<div v-bind:click="action"></div>


### 2. v-if、v-else指令

v-if、v-else:是vue 的一个内部指令，指令用在我们的html中。v-if和v-else需要配和在一起使用。

v-if指令用于判断是否加载html的DOM，比如我们模拟一个用户登录状态，在用户登录后现实用户名称。

	<template>
	  <div>
	    <div v-if="isLogin">你好：CoCo</div>
	    <div v-else>请登录后操作</div>
	  </div>
	</template>
	
	<script>
	export default {
	  data () {
	    return {
	      isLogin: true
	    }
	  }
	}
	</script>

在vue的data里定义了isLogin的值，当它为true时，网页就会显示：你好：CoCo，如果为false时，就显示请登录后操作。


### 3. v-show指令

v-show指令: 用于调整css中的display属性。 如果isShow为true，则div属性中display属性为block。如果isShow为false，则div属性中display属性为none。

	<template>
	  <div>
		// v-show指令
	    <div v-show="isShow">你好：CoCo</div>
	  </div>
	</template>
	
	<script>
	export default {
	  data () {
	    return {
	      isShow: true
	    }
	  }
	}
	</script>

### 4. v-for指令

v-for指令是循环渲染一组data中的数组，v-for 指令需要以 item in items 形式的特殊语法，items 是源数据数组并且item是数组元素迭代的别名。

	<template>
	  <div>
		<!-- v-for指令 -->
	    <li v-for="item in items">
	      {{item}}
	    </li>
	    
	    <li v-for="(key, value) in objs">
	      {{key}}-{{value}}
	    </li>
	
	    <li v-for="(value, key, index) in objs">
	      {{index}}-{{value}}-{{key}}
	    </li>
	  </div>
	</template>
	
	<script>
	export default {
	  data () {
	    return {
	      items:[20,23,18,65,32,19,54,56,41],
		  objs: {
	        name: '老王',
	        detail: '你有事情我帮忙，我住隔壁我姓王!',
	        score: 99,
	        age: 18
	      }
	    }
	  }
	}
	</script>

### 5. 


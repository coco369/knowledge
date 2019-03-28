
# vue使用操作指南--vue数据引入与修改

>Auth: 王海飞
>
>Data：2019-02-26
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge


### 1. 数据的外部引入

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在构造器外部操作定义构造器内部的数据、属性或者方法。比如在vue构造器外部定义了一个score为1的数据，我们在构造器外部定义了一个方法，要每次点击按钮给值加1，就需要用到Vue.set。

如: 在export default的外部定义outData变量，在export default的内部指定data的值。

	var outData = {
	  title: 'v-on绑定点击事件',
	  score: '0',
	  color: 'blue',
	  detail: 'hello qianfeng',
	  message: 'hello Vue!',
	  msgHtml: '<h2>hello Vue!</h2>'
	}
	
	export default {
	  // 引用外部数据
	  data () {
	    return outData
	  }
	}


### 2. 定义点击事件，修改outData中变量的值

#### 2.1 修改变量

	<template>
	  <div>
	    {{ score }}
	    <!-- v-on指令 -->
	    <p v-on:click="add()"> 加法 </p>
	    <p @click="sub()">减法</p>
	  </div>
	</template>
	
	<script>
	
	var outData = {
	  score: '0'
	}
	
	import Vue from 'vue/dist/vue.js'
	export default {
	  // 引用外部数据
	  data () {
	    return outData
	  },
	  methods: {
	    add: function () {
	      // score变量自增1
	      // this.score++
	      // outData.score++
	      Vue.set(outData, 'score', 1)
	      alert('实现加一功能')
	    },
	    sub: function () {
	      // score变量自减1
	      this.score--
	      alert('实现减一功能')
	    }
	  }
	}
	</script>

在外部改变数据的三种方法总结:

1）使用this.score++或者this.score--的方式。

2）直接操作外部数据。使用outData.score++或outData.score--的方式。

3）使用Vue.set(outData，'score'，修改后的值)。



#### 2.2 修改数组

定义在模板中解析的数组arr:

	var outData = {
	  arr: [1, 2, 3, 4, 5]
	}

在模板中使用v-for指令解析变量arr:

    <ul>
      <li v-for=" aa in arr">{{aa}}</li>
    </ul>

定义引入外部变量outData和通过点击事件实现页面中数组arr打印的渲染:
	
	import Vue from 'vue/dist/vue.js'
	export default {
	  // 引用外部数据
	  data () {
	    return outData
	  },
	  methods: {
	    add: function () {
	      // score变量自增1
	      // this.arr[1]++
	  	  // outData.arr[1]++
	      Vue.set(outData.arr, 0, 10)
	      alert('实现加一功能')
	    },
	  }
	}

本案例中定义了数组变量arr，并通过点击事件实现修改数组arr中的第二个元素的值,修改方法分为三种:

1）使用this.arr[1]++的方式。

2）直接操作外部数据。使用outData.arr[1]++的方式。

3）使用Vue.set修改第一个元素的值，如: Vue.set(outData.arr, 0, 10)。


<b>注意:</b> 前两种方式和第三种方式在渲染页面时有区别，前面两种形式修改数组的数据，但页面不刷新，而第三种形式使用Vue.set才会渲染页面。

因此Vue.set的存在原因如下:

	由于Javascript的限制，Vue不能自动检测以下变动的数组。
	
		当你利用索引直接设置一个项时，vue不会为我们自动更新。
		当你修改数组的长度时，vue不会为我们自动更新。

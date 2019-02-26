
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
	
	    <li v-for="(key, value, index) in objs">
	      {{index}}-{{key}}-{{value}}
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

<b>注意</b> : 使用v-for指令进行循环获取数据，如objs变量，通过v-for="(key, value, index) in objs"进行取值，key为objs中的value值，value为objs中的key值，index为循环的序号(从1开始)

### 5. v-on 绑定事件监听器

v-on指令监听DOM事件来触发一些javascript代码。

如下: 定义两个点击事件，并触发弹窗
	
	<template>
	  <div>
		// 打印score变量的值
	    {{ score }}
	    <!-- v-on指令 -->

	    <p v-on:click="show()"> 今天天气如何? </p>
	    <p @click="showContent()">千锋教育怎么样？</p>
	
	  </div>
	</template>
	
	<script>
	export default {
	  data () {
	    return {
	      title: 'v-on绑定点击事件',
	      score: '0'
	    }
	  },
	  methods: {
	    show: function () {
	      // score变量自增1
	      this.score++
	      alert('今天天气棒棒哒')
	    },
	    showContent: function () {
	      // score变量自减1
	      this.score--
	      alert('好好好')
	    }
	  }
	}

使用<b>v-on:click="点击调用函数"</b>或者<b>@click="点击调用函数"</b>的形式进行绑定点击事件，点击事件的定义在methods中定义。

### 5. v-bind 绑定属性


v-bind是处理HTML中的标签属性的，例如img标签，绑定src属性，进行动态赋值。

在标签template中定义如下的内容，使用v-bind进行属性的绑定:

    <!-- 属性绑定 v-bind -->
    <p v-bind:class="color">
      点我可以变换颜色哦，这是真的!
    </p>
    <p :class="color"> 简写方式 </p>

<b>注意:</b> 使用v-bind给标签绑定class属性，在页面中查看源码，可发现源码为: <p class="color">


如下:绑定src属性

	<div>
	    <img v-bind:src="imgSrc"  width="200px">
	</div>

默认样式color的定义和imgSrc的定义如下:

	export default {
	  data () {
	    return {
		  imgSrc='图片的地址',
	      color: 'blue'
	    }
	  }
	}

<b> 重点: 绑定CSS样式</b>

在工作中我们经常使用v-bind来绑定css样式：
	
在绑定CSS样式是，绑定的值必须在vue中的data属性中进行声明。 

1、直接绑定class样式
	
	<div :class="className">1、绑定classA</div>

2、绑定classA并进行判断，在isOK为true时显示样式，在isOk为false时不显示样式。
	
	<div :class="{classA:isOk}">2、绑定class中的判断</div>

3、绑定class中的数组
	
	<div :class="[classA,classB]">3、绑定class中的数组</div>

4、绑定class中使用三元表达式判断
	
	<div :class="isOk?classA:classB">4、绑定class中的三元表达式判断</div>

5、绑定style
	
	<div :style="{color:red,fontSize:font}">5、绑定style</div>

6、用对象绑定style样式
	
	<div :style="styleObject">6、用对象绑定style样式</div>
	var app=new Vue({
	   el:'#app',
	   data:{
	       styleObject:{
	           fontSize:'24px',
	           color:'green'
	            }
	        }
	})

### 6. v-model指令

v-model指令: 绑定数据源。 就是把数据绑定在特定的表单元素上，可以很容易的实现双向数据绑定。

	<!-- 双向数据绑定 v-model -->
    <p>
      <input type="text" v-model="detail">
    </p>
    <p>{{detail}}</p>


	<script>
	export default {
	  data () {
	    return {
	      detail: 'hello qianfeng'
	    }
	  }
	}
	</script>

如下图效果:

![图](../images/vue_v_model.png)

### 7. v-html/v-text

在vue文件中解析输出data中的变量时，使用{{ 变量名 }}的形式。 但这种情况是有弊端的，就是当我们网速很慢或者javascript出错时，会暴露我们的{{ 变量名 }}。Vue给我们提供的v-text,就是解决这个问题的。而v-html可以渲染输出真正的HTML，如h2标签。需要注意的是：在生产环境中动态渲染HTML是非常危险的，因为容易导致XSS攻击。所以只能在可信的内容上使用v-html，永远不要在用户提交和可操作的网页上使用。

    <div>
      <span>{{ message }}</span>=<span v-text="message"></span><br/>
      <span v-html="msgHtml"></span>
    </div>

	<script>
	export default {
	  data () {
	    return {
	      message: 'hello Vue!',
	      msgHtml: '<h2>hello Vue!</h2>'
	    }
	  }
	}
	</script>

总结: v-text只能解析变量内容，而v-html可以解析内容中带有的标签属性。
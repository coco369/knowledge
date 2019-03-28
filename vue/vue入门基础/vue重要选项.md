
# vue使用操作指南--vue重要选项

>Auth: 王海飞
>
>Data：2019-03-01
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge


### 1. computed计算属性

computed计算属性: 可以像绑定普通属性一样在模板中绑定计算属性。Vue 知道 showScore变量 依赖于 score变量，因此当 score变量 发生改变时，所有依赖 score变量 的绑定也会更新。	

	<script>
	var outData = {
	  score: '57'
	}
	
	export default {
	  // 引用外部数据
	  data () {
	    return outData
	  },
	  methods: {
	    show: function () {
	      // score变量自增1
	      this.score++
	    },
	  computed: {
	    // 使用和属性一样，但可以根据属性不同，进行动态变化
	    showScore: function () {
	      // this指向Vue实例
	      if (this.score >= 60) {
	        return '我已经及格!'
	      } else {
	        return '别骗我，我还未及格!'
	      }
	    },
	    computedLength: function () {
	      return this.score.length
	    }
	  },
	}
	</script>


### 2. watch监听

watch监听属性: 监听参数

案例1: 监听当前页面中路由地址的变化

	export default {
	watch: {
	    $route (to, from) {
	      console.log(to)
	      console.log(from)
	    }
	  }
	}

案例2: 监听页面中msg变量的值的变化

	export default {
	  watch: {
	    msg (val, oldval) {
	      console.log(val)
	      console.log(oldval)
	    }
	  }
	}

### 3. 父组件给子组件传值


### 4. 子组件给父组件传值
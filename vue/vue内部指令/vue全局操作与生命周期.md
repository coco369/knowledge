
# vue使用操作指南--vue全局操作与生命周期

>Auth: 王海飞
>
>Data：2019-02-26
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge


### 1. 全局操作

Vue.set 的作用就是在构造器外部操作构造器内部的数据、属性或者方法。比如在vue构造器内部定义了一个count为1的数据，我们在构造器外部定义了一个方法，要每次点击按钮给值加1.就需要用到Vue.set。



#### git使用规范

​		目前有主分支master branch 和开发分支develop branch ，主分支和开发分支是受保护的，开发者不能直接对其进行开发工作，只有项目管理者（通常是项目的发起者）能对其进行较高权限的操作。

​		协同开发过程开发者的工作流程是先将远程库克隆到本地库，然后基于开发分支创建一个功能分支，进行相应的功能开发后提交并推送到远程库。

![](images\git使用流程1.png)

#### 常用分支

主分支master、测试分支test、开发分支dev、个人分支xxx 

项目中长期存在的两个分支

- `master`：主分支，负责记录上线版本的迭代，该分支代码与线上代码是完全一致的。
- `test`: 测试分支，负责测试即将上线版本的功能，所有的feature分支和bugfix分支都从该分支创建。
- `dev`：开发分支，该分支用于开发集成测试，确保开发代码自测通过。

其它分支为短期分支，其完成功能开发之后需要删除

- `bugfix/*`：bug修复分支，用于修复不紧急的bug，普通bug均需要从**test**分支创建bugfix分支开发，开发完成自测没问题后合并到 **dev** 分支后，删除该分支。
- `hotfix/*`：紧急bug修复分支，该分支只有在紧急情况下使用，从**master**分支创建，用于紧急修复线上bug，修复完成后，需要合并该分支到**master**分支以便上线，同时需要再合并到**test、dev **分支。



#### 主分支master

代码库应该有一个、且仅有一个主分支。所有提供给用户使用的正式版本，都在这个主分支上发布。

![](images\master-branch.png)



#### 测试分支test

​		代码库中可以有多个测试分支，用于提供给测试人员进行多轮测试。如果测试分支功能没问题，可合并test分支到master主分支，然后进行发布。

![](F:\workspace\knowledge\代码规范\images\test-branch.png)



#### 开发分支dev

​		代码库中只有一个，主要用于集成所有开发分支的代码。如该分支代码自测存在问题，需在功能开发分支fix后，重新合并到dev分支。

![](images\dev-branch.png)

#### 紧急bug修复hotfix分支

​		紧急bug修复分支，该分支只有在紧急情况下使用，从**master**分支创建，用于紧急修复线上bug。

![](images\hoxfi-branch.png)

​		软件正式发布以后，难免会出现bug。这时就需要创建一个分支，进行bug修补。修补bug分支是从Master分支上面分出来的。修补结束以后，再合并进**Master**和**Dev** 分支。它的命名，可以采用fixbug-*的形式。



#### 分支合并

Git创建Dev分支的命令：

> 　　git checkout -b dev

将Dev分支发布到Master分支的命令：

> 　　切换到Master分支
> 　　git checkout master
>
> 　　对Develop分支进行合并
> 　　git merge --no-ff dev

这里稍微解释一下，上一条命令的--no-ff参数是什么意思。默认情况下，Git执行"快进式合并"（fast-farward merge），会直接将Master分支指向Dev分支。

![img](images\merge1.png)

使用--no-ff参数后，会执行正常合并，在Master分支上生成一个新节点。为了保证版本演进的清晰，我们希望采用这种做法。

![img](images\merge2.png)
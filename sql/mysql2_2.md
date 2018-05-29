
# Mysql数据库使用练习2

>Auth: 王海飞
>Data：2018-04-15
>Email：779598160@qq.com
>github：https://github.com/coco369/knowledge

#### 设计背景


    该练习主要针对人力资源管理系统而设计，其中设计到三张表，分别为部门表，员工表。
    部门表主要用于存储部门名称，地址等信息
    员工表主要用于存储员工姓名，职位，上级主管编号，月薪，部门编号等信息

##### 表创建/数据准备

```
-- 创建人力资源管理系统数据库
drop database if exists HR;
create database HR default charset utf8;
-- 切换数据库上下文环境
use HR;
drop table if exists TbEmp;
drop table if exists TbDept;
-- 创建部门表
create table TbDept
(
deptno tinyint primary key,	-- 部门编号
dname varchar(10) not null,	-- 部门名称
dloc varchar(20) not null	-- 部门所在地
);
-- 添加部门记录
insert into TbDept values (10, '会计部', '北京');
insert into TbDept values (20, '研发部', '成都');
insert into TbDept values (30, '销售部', '重庆');
insert into TbDept values (40, '运维部', '深圳');
-- 创建员工表
create table TbEmp
(
empno int primary key,		-- 员工编号
ename varchar(20) not null,	-- 员工姓名
job varchar(20) not null,	-- 员工职位
mgr int,			-- 主管编号
sal int not null,		-- 员工月薪
dno tinyint			-- 所在部门编号
);
alter table TbEmp add constraint fk_dno foreign key (dno) references TbDept(deptno);
-- 添加员工记录
insert into TbEmp values (7800, '张三丰', '总裁', null, 9000, 20);
insert into TbEmp values (2056, '乔峰', '分析师', 7800, 5000, 20);
insert into TbEmp values (3088, '李莫愁', '设计师', 2056, 3500, 20);
insert into TbEmp values (3211, '张无忌', '程序员', 2056, 3200, 20);
insert into TbEmp values (3233, '丘处机', '程序员', 2056, 3400, 20);
insert into TbEmp values (3251, '张翠山', '程序员', 2056, 4000, 20);
insert into TbEmp values (5566, '宋远桥', '会计师', 7800, 4000, 10);
insert into TbEmp values (5234, '郭靖', '出纳', 5566, 2000, 10);
insert into TbEmp values (3344, '黄蓉', '销售主管', 7800, 3000, 30);
insert into TbEmp values (1359, '胡一刀', '销售员', 3344, 1800, 30);
insert into TbEmp values (4466, '苗人凤', '销售员', 3344, 2500, 30);
insert into TbEmp values (3244, '欧阳锋', '程序员', 3088, 3200, 20);
insert into TbEmp values (3577, '杨过', '会计', 5566, 2200, 10);
insert into TbEmp values (3588, '朱九真', '会计', 5566, 2500, 10);
```

##### 题目练习

```
-- 查询薪资最高的员工姓名和工资
select ename, sal from TbEmp where sal=(select max(sal) from TbEmp);
-- 查询员工的姓名和年薪(月薪*12)
select ename, sal*12 as annSal from TbEmp;
-- 查询有员工的部门的编号和人数
select dno, count(dno) from TbEmp group by dno;
-- 查询所有部门的名称和人数
select dname, ifnull(total, 0) from TbDept t1 left outer join
(select dno, count(dno) as total from TbEmp group by dno) t2
on deptno=dno;
-- 查询薪资最高的员工(Boss除外)的姓名和工资
select ename, sal from TbEmp where sal=(select max(sal) from TbEmp where mgr is not null);
-- 查询薪水超过平均薪水的员工的姓名和工资
select ename, sal from TbEmp where sal>(select avg(sal) from TbEmp);
-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资
-- 写法1:
select ename, sal, t1.dno from TbEmp as t1,
(select dno, avg(sal) as avgSal from TbEmp group by dno) as t2 
where t1.dno=t2.dno and t1.sal>t2.avgSal;
-- 写法2:
select ename, sal, t1.dno from TbEmp as t1 inner join
(select dno, avg(sal) as avgSal from TbEmp group by dno) as t2 
on t1.dno=t2.dno and t1.sal>t2.avgSal;
-- 查询部门中薪水最高的人姓名、工资和所在部门名称
select ename, sal, dname from TbDept as t1 inner join
(select ename, sal, t2.dno from TbEmp as t2 inner join
(select dno, max(sal) as maxSal from TbEmp group by dno) t3
on t2.dno=t3.dno and sal=maxSal) as t4 on deptno=dno;
-- 查询主管的姓名和职位
select ename, job from TbEmp where empno in 
(select distinct mgr from TbEmp where mgr is not null);
-- 查询薪资排名前3的员工姓名和工资
select ename, sal from TbEmp order by sal desc limit 3;
select ename, sal from TbEmp order by sal desc limit 0,3;
select ename, sal from TbEmp order by sal desc limit 3 offset 0;
-- 求薪水排在第4-8名雇员
select ename, sal from TbEmp order by sal desc limit 3,5;
select ename, sal from TbEmp order by sal desc limit 5 offset 3;

```

#MySQL学习笔记#

一直用数据库可视化工具操作，除了增删改查，还没有系统的学习过，开坑学习下,查漏补缺，记录些常用的命令。

#SQL语句结尾一定要有分号一定要有分号一定要有分号（重要的事说很多遍）#


#常用命令#
```
#创建数据库
create database 数据库名

#创建表
create table 表名(
		  属性名  数据类型 [完整性约束条件],
		  属性名  数据类型 [完整性约束条件],
		  ...
		  属性名  数据类型 [完整性约束条件],
		  );

#完整约束条件包括
PRIMARY KEY 主键
FOREIGN KEY 外键
NOT NULL 不为空
UNIQUE 唯一
AUTO_INCREMENT 自增
DEFAULT 默认值


#显示数据库列表
show databases;

#使用其中某个数据库
use database_name;

#查看某个数据库中所有的表
show table status from your_table_name;

#查看某个表的所有字段
select COLUMN_NAME from information_schema.COLUMNS where table_name = 'your_table_name';

#查看某个表的所有值
select * from your_table_name;

#删除某个数据库(还是不学了)



```


#MySQL Innodb特点及优缺点#

他支持自增的主键，也支持外键，外键所依赖的表为父表，外键所在的表为子表。
它的优势是提供了良好的事务管理，崩溃修复，并发控制能力。缺点是读写效率差，占用空间大。




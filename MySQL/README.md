#MySQL学习笔记#

一直用数据库可视化工具操作，除了增删查改，啥都不会，开坑学习下,记录些常用的命令。

```
#创建数据库
create database 数据库名

#显示数据库列表（结尾的分号不能少）
show databases;

#查看某个数据库中所有的表
show table status from your_table_name;

#查看某个表的所有字段
select COLUMN_NAME from information_schema.COLUMNS where table_name = 'your_table_name';

#查看某个表的所有值
select * from your_table_name;

```
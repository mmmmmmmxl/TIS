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

#查看某个表的信息
DESCRIBE 表名;

#查看某个表的所有值
select * from your_table_name;

#删除某个数据库(还是不学了)

#查看某表的建表语句
SHOW CREATE TABLE 表名

#查询中可以带 IN，BETWEEN AND，LIKE等，相应的也可以带上NOT
SELECT * FROM TABLE WHERE COLUM BETWEEN 5 AND 20;
SELECT * FROM TABLE WHERE COLUM NOT BETWEEN 5 AND 20;
SELECT * FROM TABLE WHERE COLUM IN (1001,1004);
SELECT * FROM TABLE WHERE COLUM LIKE 'a';

#数据库中查询空值
SELECT * FROM TABLE WHERE COLUM IS NULL;

#带AND或者OR多条件查询
SELECT * FROM TABLE WHERE COLUM1 = 'ZZ' AND COLUM2 ='AA';
SELECT * FROM TABLE WHERE COLUM1 = 'ZZ' OR  COLUM2 ='AA';

#用LIMIT限制数据显示的数目,也可以用LIMIT指定查询的起始位置
SELECT * FROM TABLE LIMIT 'NUMBER';
SELECT * FROM TABLE LIMIT 0,6;

#查询指定字段
SELECT COLUM1,COLUM2,COLUM3 FROM TABLES;

#查询指定数据
SELECT * FROM TABLES WHERE COLUMS = '';

#消除重复的查询结果
SELECT DISTINACT COLUM FROM TABLES;

#对查询结果排序，可选DESC按照升序排列
SELECT COLUM1,COLUM2,COLUM3 FROM TABLES ORDER BY COLUM1 [DESC]；

#内连接，外连接
场景太多懒得写 orz

#带EXISTS关键字的子查询  （假如EXISTS里存在数据则执行查询）
SELECT * FROM TABLES WHERE EXISTS (SELECT * FROM TABLES WHERE COLUM = 'TEST')

#带ANY/ALL关键字的子查询 （只要score大于等于查询中任一条记录的score则执行，逻辑同ALL）
SELECT * FROM TABLES WHERE score>=ANY/ALL（SELECT score FROM TABLE）

#合并查询结果
SELECT * FROM TABLE1 WHERE COLUMS = '1' union SELECT * FROM TABLE2 WHERE COLUMS = '2';

#为字段取别名
SELECT COLUM1 AS C1，COLUM2 AS C2 FROM TABLES WHERE C1 = '##',C2 = '##';

#MySQL同样支持正则表达式
SELECT * FROM TABLES WHERE name REGEXP '正则表达式'

#创建新的记录
INSERT INTO TABLE_NAME VALUES ('1','NAME'...)

#更新当前记录
UPDATE TABLE_NAME SET COLUM = '' WHERE ...

#删除记录
DELETE FROM TABLE_NAME WHERE id = 1;

#

```
#MySQL中删除外键需要注意的事项#
由于在MySQL中在创建表时，若表中包含外键，外键约束就已经设定好了。
在删除外键时，需要先解除外键约束，再删除外键。
```
ALTER TABLE 表名 DROP FOREIGN KEY 外键别名;
#之后再删除该外键字段
ALTER TABLE 表名 DROP 字段名;

```
#MySQL Innodb特点及优缺点#

他支持自增的主键，也支持外键，外键所依赖的表为父表，外键所在的表为子表。
它的优势是提供了良好的事务管理，崩溃修复，并发控制能力。缺点是读写效率差，占用空间大。




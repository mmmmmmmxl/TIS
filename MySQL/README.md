#MySQLѧϰ�ʼ�#

һֱ�����ݿ���ӻ����߲�����������ɾ�Ĳ飬��û��ϵͳ��ѧϰ��������ѧϰ��,��©��ȱ����¼Щ���õ����

#SQL����βһ��Ҫ�зֺ�һ��Ҫ�зֺ�һ��Ҫ�зֺţ���Ҫ����˵�ܶ�飩#


#��������#
```
#�������ݿ�
create database ���ݿ���

#������
create table ����(
		  ������  �������� [������Լ������],
		  ������  �������� [������Լ������],
		  ...
		  ������  �������� [������Լ������],
		  );

#����Լ����������
PRIMARY KEY ����
FOREIGN KEY ���
NOT NULL ��Ϊ��
UNIQUE Ψһ
AUTO_INCREMENT ����
DEFAULT Ĭ��ֵ


#��ʾ���ݿ��б�
show databases;

#ʹ������ĳ�����ݿ�
use database_name;

#�鿴ĳ�����ݿ������еı�
show table status from your_table_name;

#�鿴ĳ����������ֶ�
select COLUMN_NAME from information_schema.COLUMNS where table_name = 'your_table_name';

#�鿴ĳ���������ֵ
select * from your_table_name;

#ɾ��ĳ�����ݿ�(���ǲ�ѧ��)



```


#MySQL Innodb�ص㼰��ȱ��#

��֧��������������Ҳ֧�����������������ı�Ϊ����������ڵı�Ϊ�ӱ�
�����������ṩ�����õ�������������޸�����������������ȱ���Ƕ�дЧ�ʲռ�ÿռ��




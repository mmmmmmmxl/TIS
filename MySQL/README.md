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

#�鿴ĳ�������Ϣ
DESCRIBE ����;

#�鿴ĳ���������ֵ
select * from your_table_name;

#ɾ��ĳ�����ݿ�(���ǲ�ѧ��)

#�鿴ĳ��Ľ������
SHOW CREATE TABLE ����

#��ѯ�п��Դ� IN��BETWEEN AND��LIKE�ȣ���Ӧ��Ҳ���Դ���NOT
SELECT * FROM TABLE WHERE COLUM BETWEEN 5 AND 20;
SELECT * FROM TABLE WHERE COLUM NOT BETWEEN 5 AND 20;
SELECT * FROM TABLE WHERE COLUM IN (1001,1004);
SELECT * FROM TABLE WHERE COLUM LIKE 'a';

#���ݿ��в�ѯ��ֵ
SELECT * FROM TABLE WHERE COLUM IS NULL;

#��AND����OR��������ѯ
SELECT * FROM TABLE WHERE COLUM1 = 'ZZ' AND COLUM2 ='AA';
SELECT * FROM TABLE WHERE COLUM1 = 'ZZ' OR  COLUM2 ='AA';

#��LIMIT����������ʾ����Ŀ,Ҳ������LIMITָ����ѯ����ʼλ��
SELECT * FROM TABLE LIMIT 'NUMBER';
SELECT * FROM TABLE LIMIT 0,6;

#
```
#MySQL��ɾ�������Ҫע�������#
������MySQL���ڴ�����ʱ�������а�����������Լ�����Ѿ��趨���ˡ�
��ɾ�����ʱ����Ҫ�Ƚ�����Լ������ɾ�������
```
ALTER TABLE ���� DROP FOREIGN KEY �������;
#֮����ɾ��������ֶ�
ALTER TABLE ���� DROP �ֶ���;

```
#MySQL Innodb�ص㼰��ȱ��#

��֧��������������Ҳ֧�����������������ı�Ϊ����������ڵı�Ϊ�ӱ�
�����������ṩ�����õ�������������޸�����������������ȱ���Ƕ�дЧ�ʲռ�ÿռ��




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

#��ѯָ���ֶ�
SELECT COLUM1,COLUM2,COLUM3 FROM TABLES;

#��ѯָ������
SELECT * FROM TABLES WHERE COLUMS = '';

#�����ظ��Ĳ�ѯ���
SELECT DISTINACT COLUM FROM TABLES;

#�Բ�ѯ������򣬿�ѡDESC������������
SELECT COLUM1,COLUM2,COLUM3 FROM TABLES ORDER BY COLUM1 [DESC]��

#�����ӣ�������
����̫������д orz

#��EXISTS�ؼ��ֵ��Ӳ�ѯ  ������EXISTS�����������ִ�в�ѯ��
SELECT * FROM TABLES WHERE EXISTS (SELECT * FROM TABLES WHERE COLUM = 'TEST')

#��ANY/ALL�ؼ��ֵ��Ӳ�ѯ ��ֻҪscore���ڵ��ڲ�ѯ����һ����¼��score��ִ�У��߼�ͬALL��
SELECT * FROM TABLES WHERE score>=ANY/ALL��SELECT score FROM TABLE��

#�ϲ���ѯ���
SELECT * FROM TABLE1 WHERE COLUMS = '1' union SELECT * FROM TABLE2 WHERE COLUMS = '2';

#Ϊ�ֶ�ȡ����
SELECT COLUM1 AS C1��COLUM2 AS C2 FROM TABLES WHERE C1 = '##',C2 = '##';

#MySQLͬ��֧��������ʽ
SELECT * FROM TABLES WHERE name REGEXP '������ʽ'

#�����µļ�¼
INSERT INTO TABLE_NAME VALUES ('1','NAME'...)

#���µ�ǰ��¼
UPDATE TABLE_NAME SET COLUM = '' WHERE ...

#ɾ����¼
DELETE FROM TABLE_NAME WHERE id = 1;

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




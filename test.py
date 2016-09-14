#! /usr/bin/env python
# coding:utf-8

import MySQLdb

db_config = {
	'host':'localhost',
	'port':3306,
	'user':'zhu',
	'passwd':'123',
	'db':'test1'
}
sql1 = '''
	create table `test_connector`(
	`id` int PRIMARY KEY auto_increment,
	`name` varchar(10) NOT NULL
)
'''
sql2 = '''
	SHOW TABLES
'''
conn = MySQLdb.connect(**db_config)
cur = conn.cursor()
cur.execute(sql1)
cur.execute(sql2)
for i in cur:
	print i
cur.close()
conn.close()

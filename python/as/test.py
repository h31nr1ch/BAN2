import MySQLdb
con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='221488',db='testepy')
c = con.cursor()

def insert(c,tabelas,what):
	c.execute("insert into "+ tabelas +" values"+ what +";")
	con.commit()

tabelas = 'modelos'
what = '(150,20,30)'
print what
insert(c,tabelas,what)


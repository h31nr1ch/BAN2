import MySQLdb
con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='221488',db='testepy')
c = con.cursor()

c.execute("insert into modelos values (2,1000,-10);")
c.execute("insert into modelos values (3,1000,10);")
c.execute("delete from modelos where modelos.capacidade < 0;")
con.commit()

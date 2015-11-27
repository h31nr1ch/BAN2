import MySQLdb

con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='221488',db='testepy')

c = con.cursor()


con.commit()

import MySQLdb
con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='221488',db='testepy')
c = con.cursor()


c.execute("drop table pericia;")
c.execute("drop table afiliacao;")
c.execute("drop table manutencao;")
c.execute("drop table controladores;")
c.execute("drop table tecnicos;")
c.execute("drop table funcionarios;")
c.execute("drop table aviao;")
c.execute("drop table testes;")
c.execute("drop table sindicatos;")
c.execute("drop table modelos;")
con.commit()


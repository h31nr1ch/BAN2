#!/usr/bin/python2.7
import MySQLdb
#http://www.programeempython.com.br/blog/bancos-de-dados-com-python-mysql/
con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='221488',db='testepy')
c = con.cursor()
#versao do db

class passt:
	def create_tables(self,c):
		c.execute("create table modelos(cod_modelo int,peso double,capacidade int,PRIMARY KEY (cod_modelo));")
	#	c.execute("insert into modelos values (1,1000,10);")
		con.commit()
		c.execute("create table sindicatos(num_sindicado int,nome varchar(50),PRIMARY KEY (num_sindicado));")
	#	c.execute("insert into sindicatos values (10,'Shane');")
		con.commit()
		c.execute("create table testes(num_anac_testes int,nome varchar(50),pont_max int,PRIMARY KEY (num_anac_testes));")
	#	c.execute("insert into testes values (1,'Christopher',30);")
		con.commit()
		c.execute("create table aviao (registro int,cod_modelo_aviao int,PRIMARY KEY (registro),FOREIGN KEY (cod_modelo_aviao) REFERENCES modelos(cod_modelo));")
	#	c.execute("insert into aviao values (15,1);")
		con.commit()
		#ok
		c.execute("create table funcionarios(num_matricula_funcionarios int,nome varchar(50),PRIMARY KEY (num_matricula_funcionarios));")
	#	c.execute("insert into funcionarios values (3,'Jimmie');")
		con.commit()
		c.execute("create table tecnicos(num_matricula_tecnicos int,endereco varchar(50),telefone varchar(10),salario int,PRIMARY KEY (num_matricula_tecnicos),FOREIGN KEY (num_matricula_tecnicos) REFERENCES funcionarios(num_matricula_funcionarios));")
	#	c.execute("insert into tecnicos values (3,'Rua Molly',11772294,3500);")
		con.commit()
		c.execute("create table controladores(num_matricula_controladores int,data_exame varchar(8),PRIMARY KEY (num_matricula_controladores),FOREIGN KEY (num_matricula_controladores) REFERENCES funcionarios(num_matricula_funcionarios));")
	#	c.execute("insert into controladores values (3,'21052015');")
		con.commit()
		c.execute("create table manutencao(num_anac_manutencao int,cod_modelo_manutencao int,num_matricula_manutencao int,data_teste varchar(8),horas_gastas double,pontuacao int, PRIMARY KEY (num_anac_manutencao),FOREIGN KEY (num_anac_manutencao) REFERENCES testes(num_anac_testes),FOREIGN KEY (cod_modelo_manutencao) REFERENCES modelos(cod_modelo),FOREIGN KEY (num_matricula_manutencao) REFERENCES funcionarios(num_matricula_funcionarios));")
	#	c.execute("insert into manutencao values (5,5,5,'10082015',2,10);")
		con.commit()
		c.execute("create table afiliacao(num_matricula_afiliacao int,num_membro int,num_sindicato_afiliacao int,PRIMARY KEY (num_matricula_afiliacao),FOREIGN KEY (num_matricula_afiliacao) REFERENCES funcionarios(num_matricula_funcionarios),FOREIGN KEY (num_sindicato_afiliacao) REFERENCES sindicatos(num_sindicado));")
	#	c.execute("insert into afiliacao values (8,18,109);")
		con.commit()
		c.execute("create table pericia(num_matricula_pericia int,cod_modelo_pericia int,PRIMARY KEY (num_matricula_pericia,cod_modelo_pericia),FOREIGN KEY (num_matricula_pericia) REFERENCES funcionarios(num_matricula_funcionarios),FOREIGN KEY (cod_modelo_pericia) REFERENCES modelos(cod_modelo));")
	#	c.execute("insert into pericia values (4,5);")
		con.commit()

	def insertts(self,c):
		c.execute("insert into modelos values (1,1000,10);")
		c.execute("insert into modelos values (2,15000,300);")
		c.execute("insert into modelos values (3,11000,200);")
		c.execute("insert into modelos values (4,12000,35);")
		c.execute("insert into modelos values (5,22000,310);")
		c.execute("insert into modelos values (6,55000,200);")
		c.execute("insert into modelos values (7,124000,150);")
		c.execute("insert into modelos values (8,13000,200);")
		c.execute("insert into modelos values (9,100000,210);")
		c.execute("insert into modelos values (10,10200,190);")
		c.execute("insert into sindicatos values (10,'Shane');")
		c.execute("insert into sindicatos values (4,'Anita');")
		c.execute("insert into sindicatos values (104,'Owens');")
		c.execute("insert into sindicatos values (105,'Milton');")
		c.execute("insert into sindicatos values (106,'Schneider');")
		c.execute("insert into sindicatos values (107,'Christopher');")
		c.execute("insert into sindicatos values (108,'Damon');")
		c.execute("insert into sindicatos values (109,'Harriet');")
		c.execute("insert into testes values (1,'Christopher',30);")
		c.execute("insert into testes values (2,'Lori',35);")
		c.execute("insert into testes values (3,'Ed Marshall',45);")
		c.execute("insert into testes values (4,'Gregory',55);")
		c.execute("insert into testes values (5,'Maria',65);")
		c.execute("insert into testes values (6,'Irving',75);")
		c.execute("insert into testes values (7,'Ed hall',45);")
		c.execute("insert into testes values (8,'Gregory',55);")
		c.execute("insert into testes values (9,'Maria',65);")
		c.execute("insert into testes values (10,'Irving',75);")
		c.execute("insert into aviao values (15,1);")
		c.execute("insert into aviao values (20,2);")
		c.execute("insert into aviao values (34,3);")
		c.execute("insert into aviao values (12,4);")
		c.execute("insert into aviao values (67,5);")
		c.execute("insert into aviao values (14,6);")
		c.execute("insert into aviao values (17,7);")
		c.execute("insert into aviao values (3,8);")
		c.execute("insert into aviao values (27,9);")
		c.execute("insert into aviao values (96,10);")
		c.execute("insert into funcionarios values (1,'Hugo');")
		c.execute("insert into funcionarios values (2,'Ebony');")
		c.execute("insert into funcionarios values (3,'Jimmie');")
		c.execute("insert into funcionarios values (4,'Israel');")
		c.execute("insert into funcionarios values (5,'Samantha');")
		c.execute("insert into funcionarios values (6,'Sabrina');")
		c.execute("insert into funcionarios values (7,'Zimmerman');")
		c.execute("insert into funcionarios values (8,'Nunez');")
		c.execute("insert into funcionarios values (9,'Beck');")
		c.execute("insert into funcionarios values (10,'Medina');")
		c.execute("insert into tecnicos values (1,'Rua Ramon',81069965,1500);")
		c.execute("insert into tecnicos values (2,'Rua Albert',55343416,2500);")
		c.execute("insert into tecnicos values (3,'Rua Molly',11772294,3500);")
		c.execute("insert into tecnicos values (4,'Rua Shari',35540971,4500);")
		c.execute("insert into tecnicos values (5,'Rua James',59764215,1670);")
		c.execute("insert into tecnicos values (6,'Rua Abraham',15830783,6500);")
		c.execute("insert into tecnicos values (7,'Rua Alfredo',41637768,8500);")
		c.execute("insert into tecnicos values (8,'Rua Nick',68665354,9500);")
		c.execute("insert into tecnicos values (9,'Rua Ignacio',10737611,5500);")
		c.execute("insert into tecnicos values (10,'Rua Wesley',16621980,1300);")
		c.execute("insert into controladores values (1,'10082015');")
		c.execute("insert into controladores values (2,'20092015');")
		c.execute("insert into controladores values (3,'21052015');")
		c.execute("insert into controladores values (4,'22052015');")
		c.execute("insert into controladores values (5,'20062015');")
		c.execute("insert into controladores values (6,'27052015');")
		c.execute("insert into controladores values (7,'20052015');")
		c.execute("insert into controladores values (8,'30052015');")
		c.execute("insert into controladores values (9,'26052015');")
		c.execute("insert into controladores values (10,'20082015');")
		c.execute("insert into manutencao values (1,1,1,'10082015',2,10);")
		c.execute("insert into manutencao values (2,2,2,'10082015',2,10);")
		c.execute("insert into manutencao values (3,3,3,'10082015',2,10);")
		c.execute("insert into manutencao values (4,4,4,'10082015',2,10);")
		c.execute("insert into manutencao values (5,5,5,'10082015',2,10);")
		c.execute("insert into manutencao values (6,6,6,'10082015',2,10);")
		c.execute("insert into manutencao values (7,7,7,'10082015',2,10);")
		c.execute("insert into manutencao values (8,8,8,'10082015',2,10);")
		c.execute("insert into manutencao values (9,9,9,'10082015',2,10);")
		c.execute("insert into manutencao values (10,10,10,'10082015',2,10);")
		c.execute("insert into afiliacao values (1,1,105);")
		c.execute("insert into afiliacao values (2,12,4);")
		c.execute("insert into afiliacao values (3,13,106);")
		c.execute("insert into afiliacao values (4,14,107);")
		c.execute("insert into afiliacao values (5,15,108);")
		c.execute("insert into afiliacao values (6,16,105);")
		c.execute("insert into afiliacao values (7,17,105);")
		c.execute("insert into afiliacao values (8,18,109);")
		c.execute("insert into afiliacao values (9,19,109);")
		c.execute("insert into afiliacao values (10,21,4);")
		c.execute("insert into pericia values (1,2);")
		c.execute("insert into pericia values (2,3);")
		c.execute("insert into pericia values (3,4);")
		c.execute("insert into pericia values (4,5);")
		c.execute("insert into pericia values (5,6);")
		c.execute("insert into pericia values (6,7);")
		c.execute("insert into pericia values (7,8);")
		c.execute("insert into pericia values (8,9);")
		c.execute("insert into pericia values (9,10);")
		c.execute("insert into pericia values (10,1);")
		con.commit()


class krl:
	def aprovados(self,c):
		c.execute("SELECT * FROM testes WHERE pont_max >= 8")
		rows = c.fetchall()
		return rows
		con.commit()

	def reprovados(self,c):
		c.execute("SELECT * FROM testes WHERE pont_max <= 5")
		rows = c.fetchall()
		return rows
		con.commit()

	def funcionarios(self,c):
		sql=c.execute("SELECT nome FROM funcionarios")
		con.commit()

	def avioes(self,c):
		sql=c.execute("SELECT cod_modelo_aviao FROM aviao")
		con.commit()

	def TRIGGER1(self,c):
		sql=c.execute("delete from modelos where modelos.capacidade < 0;")
		con.commit()

	def TRIGGER2(self,c):
		sql=c.execute("delete from testes where testes.pont_max < 0;")
		con.commit()

	def TRIGGER3(self,c):
		sql=c.execute("delete from tecnicos where tecnicos.pont_max < 0;")
		con.commit()

	def TRIGGER4(self,c):
		sql=c.execute("delete from manutencao where manutencao.horas_gastas < 0;")
		con.commit()

	def tenhado(self,c):
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

	def select(self,c,what,var):
		c.execute("select %s from %s;"%(var,what))
		con.commit()

	def update(self,c,what,update,var):
		c.execute("update %s set %s where %s;"%(what,var,update))
		con.commit()

	def dell(self,c,what,var):
		c.execute("delete from %s where %s;"%(what,var))
		con.commit()

	def insert(self,c,tabelas,what):
		#c.execute("insert into pericia values (10,1);")
		c.execute("insert into %s values %s;"%(tabelas,what))
		con.commit()
	
	def removeDaTabela(self,c,tabelas,what):
		c.execute("delete from %s where %s;"%(tabelas,what))
		con.commit()

	def buscaAviao(self,c):
		c.execute("select * from aviao order by registro;")
		rows = c.fetchall()
		return rows
#		for row in rows:
#			for col in row:
#				print (col),
#			print "\n"

	def buscaAviao3(self,c):
		c.execute("select * from aviao a join manutencao m on (m.cod_modelo_manutencao = a.cod_modelo_aviao)order by m.pontuacao;")
		rows = c.fetchall()
		return rows

	def buscaAfiliacoes(self,c):
		c.execute("select * from funcionarios s join afiliacao a on (s.num_matricula_funcionarios= a.num_matricula_afiliacao);")
		rows = c.fetchall()
		return rows

	def buscaTecnicosPericia(self,c):
		c.execute("select * from tecnicos t join pericia p on (p.num_matricula_pericia= t.num_matricula_tecnicos) join funcionarios f on (f.num_matricula_funcionarios= t.num_matricula_tecnicos);")
		rows = c.fetchall()
		return rows

	def buscaModelos(self,c):
		c.execute("select * from modelos;")
		rows = c.fetchall()
		return rows

	def buscaSindicatos(self,c):
		c.execute("select * from sindicato;")
		rows = c.fetchall()
		return rows

	def buscaSindicatos(self,c):
		c.execute("select * from sindicatos;")
		rows = c.fetchall()
		return rows

	def buscaTecnicos(self,c):
		c.execute("select * from tecnicos t join funcionarios f on (f.num_matricula_funcionarios=t.num_matricula_tecnicos);")
		rows = c.fetchall()
		return rows
"""
tenhado(c)
create_tables(c)
insertts(c)
aprovados(c)
"""

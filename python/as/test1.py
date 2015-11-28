import MySQLdb
#http://www.programeempython.com.br/blog/bancos-de-dados-com-python-mysql/
con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='221488',db='testepy')
c = con.cursor()
#versao do db

	#insert table
	#c.execute("INSERT INTO teste VALUES (13, 10,13)")
	#number of line
	#c.execute('SELECT * FROM teste')
	#print(c.execute('SELECT * FROM teste'))
	#c.fetchall()
def create_tables(c):
	c.execute("create table modelos(cod_modelo int,peso double,capacidade int,PRIMARY KEY (cod_modelo));")
	c.execute("insert into modelos values (1,1000,10);")
	con.commit()
	c.execute("create table sindicatos(num_sindicado int,nome varchar(50),PRIMARY KEY (num_sindicado));")
	c.execute("insert into sindicatos values (10,'Shane');")
	con.commit()
	c.execute("create table testes(num_anac int,nome varchar(50),pont_max int,PRIMARY KEY (num_anac));")
	c.execute("insert into testes values (1,'Christopher',30);")
	con.commit()
	c.execute("create table aviao (registro int,cod_modelo int,PRIMARY KEY (registro),FOREIGN KEY (cod_modelo) REFERENCES modelos(cod_modelo));")
	c.execute("insert into aviao values (15,1);")
	con.commit()
	c.execute("create table funcionarios(num_matricula int,nome varchar(50),PRIMARY KEY (num_matricula));")
	c.execute("insert into funcionarios values (3,'Jimmie');")
	con.commit()
	c.execute("create table tecnicos(num_matricula int,endereco varchar(50),telefone varchar(10),salario int,PRIMARY KEY (num_matricula),FOREIGN KEY (num_matricula) REFERENCES funcionarios(num_matricula));")
	c.execute("insert into tecnicos values (3,'Rua Molly',11772294,3500);")
	con.commit()
	c.execute("create table controladores(num_matricula int,data_exame varchar(8),PRIMARY KEY (num_matricula),FOREIGN KEY (num_matricula) REFERENCES funcionarios(num_matricula));")
	c.execute("insert into controladores values (3,'21052015');")
	con.commit()
#	c.execute("create table manutencao(num_anac int,cod_modelo int,num_matricula int,data_teste varchar(8),horas_gastas double,pontuacao int,PRIMARY KEY (num_anac),FOREIGN KEY (num_anac),FOREIGN KEY (cod_modelo),FOREIGN KEY (num_matricula));")
#	c.execute("insert into manutencao values (5,5,5,'10082015',2,10);")
#	con.commit()
	c.execute("create table manutencao(num_anac int,cod_modelo int,num_matricula int,data_teste varchar(8),horas_gastas double,pontuacao int,PRIMARY KEY (num_anac));")
	c.execute("insert into manutencao values (5,5,5,'10082015',2,10);")
	con.commit()
#	c.execute("create table afiliacao(num_matricula int,num_membro int,num_sindicato int,PRIMARY KEY (num_matricula),FOREIGN KEY (num_matricula),FOREIGN KEY (num_sindicato));")
#	c.execute("insert into afiliacao values (8,18,109);")
#	con.commit()
	c.execute("create table afiliacao(num_matricula int,num_membro int,num_sindicato int,PRIMARY KEY (num_matricula));")
	c.execute("insert into afiliacao values (8,18,109);")
	con.commit()
#	c.execute("create table pericia(num_matricula int,cod_modelo int,PRIMARY KEY (num_matricula,cod_modelo),FOREIGN KEY (num_matricula),FOREIGN KEY (cod_modelo));")
#	c.execute("insert into pericia values (4,5);")
#	con.commit()
	c.execute("create table pericia(num_matricula int,cod_modelo int,PRIMARY KEY (num_matricula,cod_modelo));")
	c.execute("insert into pericia values (4,5);")
	con.commit()

def aprovados(c):
	sql=c.execute("SELECT nome FROM testes WHERE pont_max >= 8")
	print(sql)
	con.commit()

def reprovados(c):
	sql=c.execute("SELECT nome FROM testes WHERE pont_max <= 5")
	print(sql)
	con.commit()

def TRIGGER1(c):
	sql=c.execute("delete from modelos where modelos.capacidade < 0;")
	con.commit()

def TRIGGER2(c):
	sql=c.execute("delete from testes where testes.pont_max < 0;")
	con.commit()

def TRIGGER3(c):
	sql=c.execute("delete from tecnicos where tecnicos.pont_max < 0;")
	con.commit()

def TRIGGER4(c):
	sql=c.execute("delete from manutencao where manutencao.horas_gastas < 0;")
	con.commit()

def tenhado(c):
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

def create(c):
	c.execute("create table %s ")
	con.commit()

def insert(c):
	con.commit()	

def delet(c,s):
	c.execute("drop table %s",s)
	con.commit()

create_tables(c)
insert(c)
aprovados(c)

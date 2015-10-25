create table modelos(cod_modelo int,peso double,capacidade int,
PRIMARY KEY (cod_modelo)
);
 
create table sindicatos(num_sindicado int,nome varchar(50),
PRIMARY KEY (num_sindicado)
);

create table testes(num_anac int,nome varchar(50),pont_max int,
PRIMARY KEY (num_anac)
);
 
create table aviao (registro int,cod_modelo int,
PRIMARY KEY (registro),
FOREIGN KEY (cod_modelo) REFERENCES modelos(cod_modelo)
);

create table funcionarios(num_matricula int,nome varchar(50),
PRIMARY KEY (num_matricula)
);

create table tecnicos(num_matricula int,endereco varchar(50),telefone varchar(10),salario int,
PRIMARY KEY (num_matricula),
FOREIGN KEY (num_matricula) REFERENCES funcionarios(num_matricula)
);

create table controladores(num_matricula int,data_exame varchar(8),
PRIMARY KEY (num_matricula),
FOREIGN KEY (num_matricula) REFERENCES funcionarios(num_matricula)
);

create table manutencao(num_anac int,cod_modelo int,num_matricula int,data_teste varchar(8),horas_gastas double,pontuacao int,
PRIMARY KEY (num_anac),
FOREIGN KEY (num_anac) REFERENCES testes(num_anac),
FOREIGN KEY (cod_modelo) REFERENCES modelos(cod_modelo),
FOREIGN KEY (num_matricula) REFERENCES funcionarios(num_matricula)
);

create table afiliacao(num_matricula int,num_membro int,num_sindicato int,
PRIMARY KEY (num_matricula),
FOREIGN KEY (num_matricula) REFERENCES funcionarios(num_matricula),
FOREIGN KEY (num_sindicato) REFERENCES sindicatos(num_sindicado)
);

create table pericia(num_matricula int,cod_modelo int,
PRIMARY KEY (num_matricula,cod_modelo),
FOREIGN KEY (num_matricula) REFERENCES funcionarios(num_matricula),
FOREIGN KEY (cod_modelo) REFERENCES modelos(cod_modelo)
);

insert into modelos values (1,1000,10);
insert into modelos values (2,15000,300);
insert into modelos values (3,11000,200);
insert into modelos values (4,12000,35);
insert into modelos values (5,22000,310);
insert into modelos values (6,55000,200);
insert into modelos values (7,124000,150);
insert into modelos values (8,13000,200);
insert into modelos values (9,100000,210);
insert into modelos values (10,10200,190);

insert into sindicatos values (10,'Shane');
insert into sindicatos values (4,'Anita');
insert into sindicatos values (104,'Owens');
insert into sindicatos values (105,'Milton');
insert into sindicatos values (106,'Schneider');
insert into sindicatos values (107,'Christopher');
insert into sindicatos values (108,'Damon');
insert into sindicatos values (109,'Harriet');

insert into testes values (1,'Christopher',30);
insert into testes values (2,'Lori',35);
insert into testes values (3,'Ed Marshall',45);
insert into testes values (4,'Gregory',55);
insert into testes values (5,'Maria',65);
insert into testes values (6,'Irving',75);
insert into testes values (7,'Ed Marshall',45);
insert into testes values (8,'Gregory',55);
insert into testes values (9,'Maria',65);
insert into testes values (10,'Irving',75);

insert into aviao values (15,1);
insert into aviao values (20,2);
insert into aviao values (34,3);
insert into aviao values (12,4);
insert into aviao values (67,5);
insert into aviao values (14,6);
insert into aviao values (17,7);
insert into aviao values (3,8);
insert into aviao values (27,9);
insert into aviao values (96,10);

insert into funcionarios values (1,'Hugo');
insert into funcionarios values (2,'Ebony');
insert into funcionarios values (3,'Jimmie');
insert into funcionarios values (4,'Israel');
insert into funcionarios values (5,'Samantha');
insert into funcionarios values (6,'Sabrina');
insert into funcionarios values (7,'Zimmerman');
insert into funcionarios values (8,'Nunez');
insert into funcionarios values (9,'Beck');
insert into funcionarios values (10,'Medina');

insert into tecnicos values (1,'Rua Ramon',81069965,1500);
insert into tecnicos values (2,'Rua Albert',55343416,2500);
insert into tecnicos values (3,'Rua Molly',11772294,3500);
insert into tecnicos values (4,'Rua Shari',35540971,4500);
insert into tecnicos values (5,'Rua James',59764215,1670);
insert into tecnicos values (6,'Rua Abraham',15830783,6500);
insert into tecnicos values (7,'Rua Alfredo',41637768,8500);
insert into tecnicos values (8,'Rua Nick',68665354,9500);
insert into tecnicos values (9,'Rua Ignacio',10737611,5500);
insert into tecnicos values (10,'Rua Wesley',16621980,1300);

insert into controladores values (1,'10082015');
insert into controladores values (2,'20092015');
insert into controladores values (3,'21052015');
insert into controladores values (4,'22052015');
insert into controladores values (5,'20062015');
insert into controladores values (6,'27052015');
insert into controladores values (7,'20052015');
insert into controladores values (8,'30052015');
insert into controladores values (9,'26052015');
insert into controladores values (10,'20082015');

insert into manutencao values (1,1,1,'10082015',2,10);
insert into manutencao values (2,2,2,'10082015',2,10);
insert into manutencao values (3,3,3,'10082015',2,10);
insert into manutencao values (4,4,4,'10082015',2,10);
insert into manutencao values (5,5,5,'10082015',2,10);
insert into manutencao values (6,6,6,'10082015',2,10);
insert into manutencao values (7,7,7,'10082015',2,10);
insert into manutencao values (8,8,8,'10082015',2,10);
insert into manutencao values (9,9,9,'10082015',2,10);
insert into manutencao values (10,10,10,'10082015',2,10);

insert into afiliacao values (1,1,105);
insert into afiliacao values (2,12,4);
insert into afiliacao values (3,13,106);
insert into afiliacao values (4,14,107);
insert into afiliacao values (5,15,108);
insert into afiliacao values (6,16,105);
insert into afiliacao values (7,17,105);
insert into afiliacao values (8,18,109);
insert into afiliacao values (9,19,109);
insert into afiliacao values (10,21,4);

insert into pericia values (1,2);
insert into pericia values (2,3);
insert into pericia values (3,4);
insert into pericia values (4,5);
insert into pericia values (5,6);
insert into pericia values (6,7);
insert into pericia values (7,8);
insert into pericia values (8,9);
insert into pericia values (9,10);
insert into pericia values (10,1);


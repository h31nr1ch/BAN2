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


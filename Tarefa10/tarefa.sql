--Descrição: Considerando o BD de uma oficina mecânica desenvolvido nas últimas aulas (e disponível na página da disciplina), faça a especificação dos seguintes gatilhos em PostgreSQL:
--1)      Gatilho para impedir a inserção ou atualização de Clientes com o mesmo CPF.
create or replace function verificaCPF() returns trigger as
$$
begin
    if(select 1 from cliente where cliente.cpf = new.cpf) then
      raise exception 'ja existe outro cliente registrado com o mesmo cpf';
    end if;
    return null;
end;
$$
language plpgsql;
CREATE TRIGGER verificaCPF BEFORE INSERT OR UPDATE ON cliente FOR EACH ROW EXECUTE PROCEDURE  verificaCPF ();
--2)      Gatilho para impedir a inserção ou atualização de Mecânicos com idade menor que 20 cerificação

create or replace function mecanicoIdade() returns trigger as
$$
begin
    if(select 1 from mecanico where new.idade>= 20) then
      raise exception 'não é permitido';
    end if;
    return null;
end;
$$
language plpgsql;
CREATE TRIGGER mecanicoIdade BEFORE INSERT OR UPDATE ON Mecanico FOR EACH ROW EXECUTE PROCEDURE  mecanicoIdade ();

--3)      Gatilho para atribuir um cods (sequencial) para um novo setor inserido.
create sequence novo_cods start 10;

create or replace function novo_cods() returns trigger as
$$
begin
    new.cods := nextval('novo_cods');
    return new;
end;
$$
language plpgsql;

create trigger novo_cods before insert on setor
    for each row execute procedure novo_cods();
    select * from setor
insert into setor (cods, nome) values ('teste');
--4)      Gatilho para impedir a inserção de um mecânico ou cliente com CPF inválido.

create or replace function inser returns trigger as
$$
begin
    if(select 1 from cliente where cliente.cpf = new.cpf) then
      raise exception 'ja existe outro cliente registrado com o mesmo cpf';
    end if;
    return null;
end;
$$
language plpgsql;
CREATE TRIGGER inser BEFORE INSERT OR UPDATE ON mecanico join cliente () FOR EACH ROW EXECUTE PROCEDURE  inser ();

--5)      Gatilho para impedir que um mecânico seja removido caso não exista outro mecânico com a mesma função.

create or replace function impedir_Mecanico() returns trigger as
$$
declare
    cont_funcao integer;
begin
    select count (*) into cont_funcao from mecanico where funcao = old.funcao;
    if cont_funcao <= 1 then
        raise exception 'Operacao impossivel';
    end if;
    return old;
end;
$$

LANGUAGE plpgsql;

create trigger impedir_Mecanico before insert or update on mecanico for each row execute procedure impedir_Mecanico();

drop function impedir_Mecanico() cascade

--6)      Gatilho que ao inserir, atualizar ou remover um mecânico, reflita as mesmas modificações na tabela de Cliente. Em caso de atualização, se o mecânico ainda não existir na tabela de Cliente, deve ser inserido.

create or replace function mec() returns trigger as
$$
begin
if select m.cpf,m. nome, m.idade, m.endereco, m.cidade from mecanico m
where NOT EXISTS ( SELECT  *
            FROM   cliente c
            WHERE   c.cpf=m.cpf and c.nome = m.nome and c.idade = m.cidade and c.idade= m.idade and c. endereco = m.endereco
    else
        set c.cpf=m.cpf and c.nome = m.nome and c.idade = m.cidade and c.idade= m.idade and c. endereco = m.endereco;

end;
$$
LANGUAGE plpgsql;
create trigger mec before insert or update on cliente for each row execute procedure mec();

--7)      Gatilho para impedir que um conserto seja inserido na tabela Conserto se o mecânico já realizou mais de 20 horas extras no mês.

create or replace function hora_max() returns trigger as
$$
declare
    hora integer default 0;
begin
    select count (*) into hora from conserto where codm = new.codm;
    if hora > 20 then
        raise exception 'Maximo de horas';
    end if;
    return new;

end;
$$
LANGUAGE plpgsql;

create trigger hora_max before insert or update on conserto for each row execute procedure hora_max();

--Nota: Para a implementação dos gatilhos devem ser utilizadas as funções implementadas no exercício 10, quando possível.


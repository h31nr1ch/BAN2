CREATE FUNCTION funcionariosApos(funcionario varchar (50))
RETURNS varchar (50)
RETURN (SELECT * FROM  testes WHERE pont_max >= 8)

CREATE FUNCTION funcionariosexames(funcionario varchar (50))
RETURNS varchar (50)
RETURN (SELECT * FROM  testes WHERE pont_max < 5)

DELIMITER $$
CREATE TRIGGER capacidadesss
BEFORE UPDATE ON modelos
FOR EACH ROW BEGIN
delete from modelos where modelos.capacidade < 0;
 END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER testnegativo
BEFORE UPDATE ON testes
FOR EACH ROW BEGIN
delete from testes where testes.pont_max < 0;
 END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER salarionegativo
BEFORE UPDATE ON tecnicos
FOR EACH ROW BEGIN
delete from tecnicos where tecnicos.pont_max < 0;
 END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER horaspositivas
BEFORE UPDATE ON manutencao
FOR EACH ROW BEGIN
delete from manutencao where manutencao.horas_gastas < 0;
 END$$
DELIMITER ;



CREATE FUNCTION funcionariosApos(funcionario varchar (50))
RETURNS varchar (50)
RETURN (SELECT *
        FROM  testes
        WHERE pont_max >= 8)

CREATE FUNCTION salario_null () 
RETURNS  
    delete FROM tecnicos
        WHERE tecnicos.salario <= 0;


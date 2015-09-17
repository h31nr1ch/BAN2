/*Descrição: Considerando o BD de uma oficina mecânica desenvolvido nas últimas aulas (e disponível na página da disciplina), faça a especificação dos seguintes gatilhos em PostgreSQL:
*/
--Nota: Para a implementação dos gatilhos devem ser utilizadas as funções implementadas no exercício 10, quando possível.

--1)      Gatilho para impedir a inserção ou atualização de Clientes com o mesmo CPF.

--2)      Gatilho para impedir a inserção ou atualização de Mecânicos com idade menor que 20 anos.

--3)      Gatilho para atribuir um cods (sequencial) para um novo setor inserido.

--4)      Gatilho para impedir a inserção de um mecânico ou cliente com CPF inválido.

--5)      Gatilho para impedir que um mecânico seja removido caso não exista outro mecânico com a mesma função.

--6)      Gatilho que ao inserir, atualizar ou remover um mecânico, reflita as mesmas modificações na tabela de Cliente. Em caso de atualização, se o mecânico ainda não existir na tabela de Cliente, deve ser inserido.

--7)      Gatilho para impedir que um conserto seja inserido na tabela Conserto se o mecânico já realizou mais de 20 horas extras no mês.


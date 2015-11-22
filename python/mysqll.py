# Importa os modulos necessarios 'MySQLdb'
import MySQLdb, time

# Define endereco do servidor, nome de usuario do bd, senha do usuario do bd e nome da base de dados
aServidor = "127.0.0.1"#localhost
aUsuario  = "dark"
aSenha    = "221488"
aBanco    = "BD"

# Realiza a conexao com o banco
db = MySQLdb.connect(aServidor, aUsuario, aSenha, aBanco)
cursor = db.cursor() # seta o cursor para a conexao

# Funcao que executa os comandos SQL no banco
def Executa_SQL(pSQL):
  try:
    cursor.execute(pSQL)
    db.commit()
  except:
    print("Erro: Nao foi possivel executar o SQL")
    db.rollback()

db.close()

time.sleep(3)

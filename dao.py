#Autora: Lorena de Jesus
#Data: 02/12/2019
#Modulo responsável por toda conexão com o banco de dados



from models import Estabelecimento, Usuario, Lista_Estab

SQL_DELETA_ESTABELECIMENTO = 'delete from programa.estabelecimento where id = %s'
SQL_ESTABELECIMENTO_POR_ID = 'SELECT  razaosocial,cnpj,email,endereco,cidade,estado,telefone,dtcadastro,categoria,status,agencia,conta,id from programa.estabelecimento where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_ESTABELECIMENTO = 'UPDATE programa.estabelecimento SET razaosocial=%s, cnpj=%s, email=%s, endereco=%s, cidade=%s, estado=%s, telefone=%s, dtcadastro=%s,categoria=%s, status=%s, agencia=%s, conta=%s where id = %s'
SQL_BUSCA_ESTABELECIMENTOS = 'SELECT id,razaosocial,cnpj,email,endereco,cidade,estado,telefone,dtcadastro,categoria,status,agencia,conta from programa.estabelecimento'
SQL_LISTA_BASICA = 'SELECT id,razaosocial,email,telefone,status from programa.estabelecimento'
SQL_CRIA_ESTABELECIMENTO = 'INSERT into programa.estabelecimento values (null,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'





class EstabelecimentoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, estab):

        cursor = self.__db.connection.cursor()

        if (estab.id):
            cursor.execute(SQL_ATUALIZA_ESTABELECIMENTO, (estab.rz_social, estab.cnpj,estab.email, estab.endereco, estab.cidade, estab.estado, estab.telefone, estab.dtcadastro, estab.categoria,estab.status, estab.agencia, estab.conta, estab.id))
        else:
            cursor.execute(SQL_CRIA_ESTABELECIMENTO,    (estab.rz_social, estab.cnpj, estab.email, estab.endereco, estab.cidade, estab.estado, estab.telefone, estab.dtcadastro, estab.categoria, estab.status, estab.agencia, estab.conta))
            estab.id = cursor.lastrowid
        self.__db.connection.commit()
        return estab

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ESTABELECIMENTOS)
        estab = traduz_estabelecimento(cursor.fetchall())
        return estab

    def listarbasica(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_BASICA)
        seila = exibe(cursor.fetchall())

        return seila
        #return Lista_Estab(seila[0], seila[1], seila[2], seila[3], seila[4],seila[5],seila[6], seila[7])

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ESTABELECIMENTO_POR_ID, (id,))
        tupla = cursor.fetchone()
        print(tupla)
        return Estabelecimento(tupla[0],tupla[1], tupla[2], tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],tupla[10],tupla[11],tupla[12])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_ESTABELECIMENTO, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_estabelecimento(estab):
    def cria_estabelecimento_com_tupla(tupla):
        return Estabelecimento(tupla[1],tupla[2], tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],tupla[10],tupla[11],tupla[12],id=tupla[0])
    return list(map(cria_estabelecimento_com_tupla, estab))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])


def exibe(seila):
    def exibedados(tupla):
        return Lista_Estab(tupla[1], tupla[2], tupla[3], tupla[4],id=tupla[0])
    return list(map(exibedados, seila))







class Estabelecimento:
    def __init__(self, _rz_social,_cnpj,_email, _endereco, _cidade, _estado, _telefone, _dtcadastro,_categoria, _status, _agencia,_conta, id=None):
        self.rz_social = _rz_social
        self.cnpj = _cnpj
        self.email = _email
        self.endereco = _endereco
        self.cidade = _cidade
        self.estado = _estado
        self.telefone = _telefone
        self.dtcadastro =  _dtcadastro
        self.categoria =_categoria
        self.status = _status
        self.agencia = _agencia
        self.conta = _conta
        self.id = id


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

class Lista_Estab:
    def __init__(self, _rz_social,_email,_telefone,_status, id=None):
        self.rz_social = _rz_social
        self.email = _email
        self.status = _status
        self.telefone = _telefone
        self.id = id
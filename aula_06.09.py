class Agenda:
    def __init__(self, nome, **dados):
        self.nome = nome
        self.contatos = []
        if 'contatos' in dados: #verificar se existe a chave 'contatos' dentro dos dados para buscar o discionário
            print('achei contatos') 
            for c in dados['contatos']:#achar cada contato e 
                self.contatos.append(c)
        else:
            print('não achei o contato')



        self.grupos = []
        if 'grupos' in dados:
            for g in dados['grupos']:
                self.grupos.append(g)
 
    def addContatos(self,c):
        self.contatos.append(c)

    def addGrupos(self,g):
        self.grupos.append(g)

    def buscarContatos(self, nome):
        #loop por todos os contatos da agenda
        for c in self.contato:
            if c.nome == nome: #compara o nome do contato
                return c
        return 'não encontrado'
    
    def buscaGrupo(self, nome):
        for g in self.grupos:
            if g.nome == nome:
                return g
        return 'não encontrado'

    def contatosGrupos(self, nome):
        pass

class Contato:
    def __init__(self, nome , tele1, *outros_tele, **dados):
        self.nome= nome
        #metodo 2
        # if 'apelido' in dados:
        #     self.apelidos = dados['apelido']
        # else:
        #     self.apelido = '(sem apelido)'#valor padão caso não encontre o apelido
        #metodo
        self.apelido = dados.pop('apelido','') #dados.pop('','') faz a mesma coisa que o de cima, é tipo um replace
        self.endereco = dados.pop('endereco','')
        self.__telefones =[tele1]
        for t in outros_tele:
            self.__telefones.append(t) 

        self.empresa = dados.pop('empresa','')
        self.cargo = dados.pop('cargo','')

        def addTelefone(self, t):
            self.__telefone.append(t)

        def listaTelefone(self):
            return self.__telefones
        
class Grupos:
    def __init__(self, nome, **dados):
        self.nome = nome
        self.criadoPor = dados.pop('criado_por','')
        self.descrição = dados.pop('descricao','')
        self.cor = dados.pop('cor','')
        self.__contatos = dados.pop('contatos',[])
        # if 'contatos' in dados:
        #     for c in dados['contatos']:
        #         self.__contatos.append(c)

        def addContatos(self, c):
            self.__contato.append(c)

        def listaContato(self ):
            return self.__contatos




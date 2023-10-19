class Crianca:
    def __init__(self,nome, **dados):
        self.nome = nome
        self.idade = dados.pop('idade',0)
        self.sexo = dados.pop('sexo','')
        self.responsavel = dados.pop('resp','')
        self.__pet = []
        if 'pets' in dados:
            for p in dados['pets']:
                self.__pet.append(p)

    def addPet(self, novoPet):
        self.__pet.append(novoPet)

    def listarPets(self):
        return self.__pet



class Pessoa:
  def __init__(self, p_nome, p_sexo, p_idade):
    self.nome = p_nome
    self.sexo = p_sexo
    self.idade = p_idade

  def aniversaria(self):
    self.idade += 1
    print(f'\033[31mParabéns {self.nome}!! \nFelicidades!!!')

  def imprimir_dados(self):
    print(f'\033[36mNome: {self.nome}')
    print(f'\033[36mSexo: {self.sexo}')
    print(f'\033[36mIdade: {self.idade}')

class Atleta(Pessoa):
  def __init__ (self, p_nome, p_sexo, p_idade):
    Pessoa.__init__(self, p_nome, p_sexo, p_idade)
  def aquecer (self):
    print('\033[96mAtleta aquecendo. ')

class Corredor(Atleta):
  def __init__ (self, p_nome, p_sexo, p_idade):
    Atleta.__init__(self,p_nome, p_sexo, p_idade)
  def correr (self):
    print('\033[96mEstou correndo...')

class Nadador(Atleta):
  def __init__ (self,p_nome,p_sexo,p_idade):
    Atleta.__init__(self, p_nome, p_sexo, p_idade)
  def nadar (self):
    print('\033[96mEstou nadando...')

class Ciclista(Atleta):
  def __init__ (self,p_nome,p_sexo,p_idade):
    Atleta.__init__(self, p_nome, p_sexo, p_idade)
  def pedalar (self):
    print('\033[96mEstou pedalando...')

class Triatleta(Corredor, Nadador, Ciclista):
  def __init__ (self, p_nome, p_sexo, p_idade):
    Corredor.__init__(self, p_nome, p_sexo, p_idade)
    Nadador.__init__(self, p_nome, p_sexo, p_idade)
    Ciclista.__init__(self, p_nome, p_sexo, p_idade)
  def iniciar_maratona(self):
    print('\033[96mAtleta iniciou a maratona...')

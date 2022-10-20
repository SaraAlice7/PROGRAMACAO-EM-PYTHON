class Pessoa:
    def __init__(self, p_nome, p_sexo, p_idade):
        self.nome = p_nome
        self.sexo = p_sexo
        self.idade = p_idade

    def aniversaria(self):
        self.idade += 1
        print(f'Parabéns {self.nome}!! \nFelicidades!!!')

    def imprimir_dados(self):
      print(f'\033[35mNome: {self.nome}')
      print(f'\033[35mSexo: {self.sexo}')
      print(f'\033[35mIdade: {self.idade}')


class Funcionario(Pessoa):
    def __init__(self, p_nome, p_sexo, p_idade):
        Pessoa.__init__(self, p_nome, p_sexo, p_idade)

        self.salario = 1100
        self.admitido = True
        self.nome = p_nome
        self.sexo = p_sexo
        self.idade = p_idade

    def mostra_admissao(self):
        return self.admitido

    def demitir(self):
        if self.mostra_admissao() == True:
            self.admitido = False
            print('\033[31mO funcionario foi demitido')
        else:
            print('\033[31mO funcionario já está fora da empresa')

    def contratar(self):
        if self.mostra_admissao() == False:
            self.admitido = True
            print('\033[32mFuncionario contratado')
        else:
            print('\033[32mO funcionario já esta na empresa')

    def aumentar_salario(self, valor):
        self.salario += valor
        print(f'\033[34mSalario definifo para {self.salario}')
        return self.salario

    def imprimir_cadastro(self):
        self.imprimir_dados()
        print(f'\033[35mSalario atual: R${self.salario}')
        print(f'\033[35mSituação na empresa de: {self.admitido}')

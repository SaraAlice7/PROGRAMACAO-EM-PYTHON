class Professor:
  def __init__(self, matricula = None, nome = None,
               idade = None, email = None):
 
    self.matricula = matricula
    self.nome      = nome
    self.idade     = idade
    self.email     = email

  def cadastra(self):
    nome_arquivo = "professor.txt"
    try:            
      arquivo = open(nome_arquivo, "r")
      linha = arquivo.readlines()
      linha.append(str(self.matricula) + "|" +
                   self.nome + "|" + str(self.idade) + "|" +
                   self.email + "\n")
      arquivo = open(nome_arquivo, "w")
      arquivo.writelines(linha)
    except IOError:
      print("ERRO: Arquivo não localizado.")
    except Exception as erro:
      print(f"ERRO: {erro}")
    else:
      print("Dados gravados com sucesso.")
    finally:
      arquivo.close()

  def lista(self):
    nome_arquivo = "professor.txt"
    try:            
      arquivo = open(nome_arquivo, "r")
      for linha in arquivo.readlines():
        campos = linha.strip()
        matricula, nome, idade, email = campos.split("|")
        print(f"Matrícula: {matricula}")
        print(f"Nome.....: {nome}")
        print(f"Idade....: {idade}")
        print(f"E-mail...: {email}\n")
       
    except IOError:
      print("ERRO: Arquivo não localizado.")
    except Exception as erro:
      print(f"ERRO: {erro}")
    finally:
      arquivo.close()

  def consulta(self, mat):
    nome_arquivo = "professor.txt"
    try:            
      arquivo = open(nome_arquivo, "r")
      for linha in arquivo.readlines():
        campos = linha.strip()
        matricula, nome, idade, email = campos.split("|")      
        if mat == int(matricula):
          print(f"Matrícula: {matricula}")
          print(f"Nome.....: {nome}")
          print(f"Idade....: {idade}")
          print(f"E-mail...: {email}\n")
          break
    except IOError:
      print("ERRO: Arquivo não localizado.")
    except Exception as erro:
      print(f"ERRO: {erro}")
    finally:
      arquivo.close()

# Testando os cadastros
# p1= Professor(123, "Procópio", 20, "fabio@gmail.com")
# p2= Professor(456, "Siqueira", 30, "siqueira@gmail.com")
# p3= Professor(789, "Eduardo", 25, "dudu@gmail.com")

# p1.cadastra()
# p2.cadastra()
# p3.cadastra()
# Testando os cadastros

# Testando as consultas
# p = Professor()
# p.lista()
# p.consulta(123)
# Testando as consultas
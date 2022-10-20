class Modelo:
  def __init__ (self, p_qtde_paraquedas):
    self.pousado = True
    self.qtde_paraquedas = p_qtde_paraquedas

  def mostra_estado(self):
    return self.pousado
  
  def decolar (self):
    if self.mostra_estado() == True:
      self.pousado = False
      self.qtde_paraquedas += 3
      print('Decolando...')
    else:
      print('\033[31mErro: Já está voando...')

  def ajustar_comandos (self):
    if self.mostra_estado() == True:
      self.pousado = False
      print('Ajustando comandos...')
    else:
      print('\033[31mErro: Modelo já está voando. Pouse o modelo para ajustar comandos...')
  
  def pousar (self):
    if self.mostra_estado() == False:
      self.pousado = True
      print('Pousando...')
    else:
      print('\033[31mErro: Já está pousado...')

  def liberar_paraquedas (self):
    if self.mostra_estado() == False:
      self.pousado = True
      self.qtde_paraquedas -= 1
      print(f'Paraquedas liberado...\nQuantidade atual de {self.qtde_paraquedas} paraquedas')
    else:
      print('\033[31mErro: Os paraquedas só podem ser liberados quando o modelo está voando')

  def retorna_qtde_paraquedas (self):
    return self.qtde_paraquedas

class Aeromodelo (Modelo):
  def alinhar_trem_pouso (self):
    if self.mostra_estado() == False:
      self.pousado = True
      print('\033[31mErro: Para ajustar o trem de pouso, o aeromodelo deve estar no solo.')
    else:
      print('Alinhando trem de pouso do aeromodelo...')

class Helimodelo (Aeromodelo):
  def pairar (self):
    if self.mostra_estado() == False:
      self.pousado = True
      print('Helimodelo pairando...')
    else:
      print('\033[31mErro: Para pairar, o helimodelo deve está voando')
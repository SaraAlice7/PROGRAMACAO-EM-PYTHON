class TabelaVerdade:
  def __init__ (self, bit1):
    self.bit1 = bit1
    
class OperadorAnd (TabelaVerdade):
  def __init__ (self, bit1, bit2):
    TabelaVerdade.__init__(self, bit1)
    self.bit2 = bit2
  def executa_operacao_logica(self):
    if self.bit1 == 1 and self.bit2 == 1:
      return True
    else:
      return False
      
class OperadorOr (TabelaVerdade):
  def __init__ (self, bit1, bit2):
    TabelaVerdade.__init__(self, bit1)
    self.bit2 = bit2
  def executa_operacao_logica(self):
    if self.bit1 == 1 or self.bit2 == 1:
      return True
    else:
      return False
      
class OperadorNot (TabelaVerdade):
  def __init__ (self, bit1):
    TabelaVerdade.__init__(self, bit1)
  def executa_operacao_logica (self):
    if self.bit1 == 1:
      return False
    else:
      return True
      
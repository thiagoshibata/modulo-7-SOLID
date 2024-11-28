from abc import ABC, abstractmethod

# BAD EXAMPLE
""" 
  class Document(ABC):
  @abstractmethod
  def load(self): pass
  
  @abstractmethod
  def view(self): pass

  @abstractmethod
  def calculate(self): pass 

  """
# A classe Excel seria obrigada a implementar View, especificamente da classe PDF, sem necessidade de uso.

# ISP - Interface Segregation Principle

class DocumentPDF(ABC):
  @abstractmethod
  def load(self): pass
  
  @abstractmethod
  def view(self): pass

class DocumentExcel(ABC):
  @abstractmethod
  def load(self): pass
  
  @abstractmethod
  def calculate(self): pass

class PDF(DocumentPDF):
  def load():
    print("Carregando o PDF")
  
  def view():
    print("Visualizando o PDF")

class Excel(DocumentExcel):
  def load():
    print("Carregando a Planilha")
  
  def calculate():
    print("Calculando a média de uma coluna")
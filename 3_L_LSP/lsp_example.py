class Animal:
  def comer(self):
    print("O animal está comendo")

class Felino(Animal):
  def lamber(self):
    print("O felino está lambendo seu pelo")

class Leao(Felino):
  def rugir(self):
    print("O Leão está rugindo alto!")

class Pessoa:
  def observa(self, animal: Animal):
    animal.comer()

animal = Animal()
felino = Felino()
leao = Leao()
pessoa = Pessoa()

# Pode se colocar qualquer subtipo de animal sem alterar o comportamento.
pessoa.observa(leao) # // O animal está comendo
# pessoa.observa(felino)
# pessoa.observa(animal)
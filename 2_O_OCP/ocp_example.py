# Bad class
""" class Company:
  def do_work(self, worker: int) -> None:
    if worker == 1:
      print('Programmer creating code')
    if worker == 2:
      print('Seller selling the product')
    if worker == 3:
      print('Human Resources hiring new devs')
    else:
      print("error, no worker!") """

# Open/Clesed Principle

class Programmer:
  def make(self):
    print("Programmer creating code")

class Seller:
  def make(self):
    print("Seller selling the product")

class Company:
  def do_work(self, worker: any) -> None:
    worker.make()

programmer = Programmer()
seller = Seller()
company = Company()
company.do_work(programmer)
company.do_work(seller)
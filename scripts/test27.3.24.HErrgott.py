class Mnozina:
    def __init__(self, prvky=None):
        if prvky is None:
            prvky = []
        self.prvky = list(prvky)

    def Obsahuje(self, prvek):
        if prvek in self.prvky:
            return True
        else:
            return False

    def pridej(self, prvek):
        if prvek not in self.prvky:
            self.prvky.append(prvek)

    def Smaz(self, prvek):
        if prvek in self.prvky:
            self.prvky.remove(prvek)

    def zobrazit_mnozinu(self):
        return self.prvky
    
    def __str__(self):
        return   " ".join(str(self.prvky)) 
    
    def __add__(self, other):
        sjednocena_mnozina = self.prvky + [prvek for prvek in other.prvky if prvek not in self.prvky]
        return Mnozina(sjednocena_mnozina)
    
  ##  def __mul__(self, other):
   #     prunik_mnozina =
   #     return Mnozina(prunik_mnozina)
    
    
A = Mnozina((1, 2, 3))
print("Původní množina:", A.zobrazit_mnozinu())

B= Mnozina((3, 2, 4, 5))
print("Původní množina:", B.zobrazit_mnozinu())

print(A.Obsahuje(1))

A.pridej(4)
print("Po přidání prvku 4:", A.zobrazit_mnozinu())

A.Smaz(2)
print("Po odebrání prvku 2:", A.zobrazit_mnozinu())

B.Smaz(3)
print("Po odebrání prvku 3:", B.zobrazit_mnozinu())

B.Smaz(10)
print("Po odebrání prvku 10:", B.zobrazit_mnozinu())

print(A)
print(B)

print("Sjednocení množin (A + B):", A + B)
#print("Průnik množin (A * B):", A * B)



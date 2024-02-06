#Poo
#Classe de exemplo
class People: 
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def hello(self):
        return f"Hello, my name is {self.name} and i have {self.age} years old."

#Objetos
pOne = People("Larissa", 23)
hello = pOne.hello()
print(hello)

pTwo = People("Gabriel", 26)
hello = pTwo.hello()
print(hello)

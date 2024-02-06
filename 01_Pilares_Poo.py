#Exemplo de Herança
    # \n significa quebra de linha
print("\nExemplo de herança:")
class Animal:
    def __init__(self, name) -> None:
        self.name = name
        
    def walk(self):
        print("The animal {self.name} walked. ")
        return
    
    def animalSound(self):
        pass
class Dog(Animal):
    def animalSound(self):
        return "Au, au"
    
class Cat(Animal):
    def animalSound(self):
        return "Miau!"


dog = Dog("Nick") #Poderia colocar nome="Nick" mas assim é melhor (poupa código).
cat = Cat("Larissinha")

print("\nExemplo de polomorfismo")
animals = [dog, cat]

for animal in animals:
    print(f"{animal.name} faz: {animal.animalSound()}")

print("\nExemplo de encapsulamento")
""" Создайте Dogкласс, родительским классом которого является этот Animalкласс. В этом Dogклассе переопределите sayметод так, 
чтобы он возвращал строку "Woof"для экземпляров этого Dogкласса.

В конструкторе класса Dogвведите новое breedсвойство. Все свойства, унаследованные от Animalкласса, должны остаться.

Создайте следующий экземпляр класса Dogв коде.

dog = Dog("Barbos", 23, "labrador") """
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)  
        self.breed = breed  

    def say(self) -> str:
        return "Woof"
dog = Dog("Barbos", 23, "labrador")    
    
""" For the previous task, let's add the Owner class - the dog's owner. The class has three attributes: name, age, and address. 
You also need to implement the info method, which returns a dictionary with the keys 'name', 'age', and 'address', and whose 
values are equal to the corresponding properties of the class instance.

You should implement the owner attribute for the Dog class, which will be an instance of the Owner class. Add to the Dog class 
the who_is_owner method, which returns the result of calling the info method of an instance of the Owner class. It will be a 
dictionary with the following keys: name, age, and address of the owner. """


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self,name, age, address):
        self.name = name
        self.age=age
        self.address=address
        
    def info(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address
        }

# The object dog should have the field owner

class Dog(Animal):   
    def __init__(self, nickname, weight, breed, owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner=owner  # Assigning an owner to the dog instance
        

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()  # Returns the owner's info as a dictionary

owner1=Owner("John", 30, "123 Street")
dog = Dog("Barbos", 23, "labrador", owner1)
print(dog.nickname)  # Output: Barbos
print(dog.weight)    # Output: 23
print(dog.breed)     # Output: labrador
print(dog.say())     # Output: Woof
print(dog.owner.info())  # Output: {'name': 'John', 'age': 30, 'address': '123 Street'} 
# dog.Owner = owner1  # Assigning an owner to the dog instance
dog_info = dog.who_is_owner()
print(dog_info)  # Output: {'name': 'John', 'age': 30, 'address': '123 Street'}

""" Create two classes: CatDog and DogCat. These classes should be inherited from two classes at once: Cat and Dog. 
After inheriting from an instance of the CatDog class, the parent say method should return Meow, and the DogCat 
class should return "Woof". For both of these classes, implement the info method returning a string in the following 
format f"{self.nickname}-{self.weight}". """
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"

class CatDog(Cat, Dog):
    def say(self):
        return "Meow"
    def info(self):
        return f"{self.nickname}-{self.weight}"

class DogCat(Cat, Dog):
    def say(self):
        return "Woof"
    def info(self):
        return f"{self.nickname}-{self.weight}"
cat_dog = CatDog("Whiskers", 10)
dog_cat = DogCat("Rex", 20)
print(cat_dog.say())  # Output: Meow
print(dog_cat.say())  # Output: Woof
print(cat_dog.info())  # Output: Whiskers-10
print(dog_cat.info())  # Output: Rex-20

""" In the fourth module, we implemented the lookup_key function to search for all keys by value in the dictionary. 
We passed the dictionary as the first parameter to the function, and the value we wanted to find as the second. 
We got a list of keys or an empty list if we didn't find anything.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
Create a LookUpKeyDict class whose parent is the UserDict class. Set the lookup_key function to be a method of the LookUpKeyDict class. """
from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys
# Example usage
data = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1})
print(data.lookup_key(1))  # Output: ['a', 'c']

""" Перепишем задачу расчета задолженности по коммунальным услугам с использованием UserListкласса.

payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
    
    Давайте вспомним условие. У нас есть список показаний задолженности по коммунальным услугам на конец месяца. 
Это paymentсписок. Долг может быть отрицательным, если у нас есть переплата, или положительным, если нам нужно 
оплатить счета.

    Создайте AmountPaymentListкласс, наследующий UserListкласс. Сделайте amount_paymentфункцию методом класса 
AmountPaymentList. """ 
from collections import UserList
class AmountPaymentList(UserList):
    def amount_payment(self):
        total = 0
        for value in self.data:
            if value > 0:
                total += value
        return total
# Example usage
payment = AmountPaymentList([1, -3, 4])
print(payment.amount_payment())  # Output: 5
       
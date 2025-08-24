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

""" Создайте NumberStringкласс, унаследуйте его от UserStringкласса и определите number_count(self)для него метод. 
Этот метод будет подсчитывать количество цифр в строке. """
from collections import UserString
class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count
# Example usage
number_string = NumberString("Hello123")
print(number_string.number_count())  # Output: 3 (since there are three digits: 1, 2, and 3)

""" Создайте IDExceptionкласс, который будет наследовать Exceptionкласс.

    Также реализуйте add_id(id_list, employee_id)функцию, которая добавляет идентификатор пользователя employee_id к 
id_list и возвращает указанный обновленный id_list.

    Функция add_idвызовет свою собственную, IDExceptionесли employee_id не начинается с 01, в противном случае 
employee_idбудет добавлена к id_list. """
class IDException(Exception):
    pass
def add_id(id_list, employee_id):
    if not employee_id.startswith("01"):
        raise IDException(f"Invalid employee ID: {employee_id}. It must start with '01'.")
    id_list.append(employee_id)
    return id_list
# Example usage
id_list = []
try:
    updated_list = add_id(id_list, "01234")
    print(updated_list)  # Output: ['01234']
    updated_list = add_id(id_list, "12345")  # This will raise IDException
except IDException as e:
    print(e)
""" Утиная типизация — это механизм в Python, позволяющий использовать любой объект вместо другого, если 
у обоих есть необходимые методы и поля. Такая типизация называется утиной типизацией из-за поговорки: 
«Если что-то крякает как утка, плавает как утка и летает как утка, то это утка». Это отражает суть подхода, 
реализованного в Python. Нет, интерпретатор не проверяет, что объект требуемого или дочернего класса 
передан функции или методу. Достаточно, чтобы объект имел необходимые методы, и всё будет работать.

class Mammal:
    phrase = ''

    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)  # Recorded "Meow!"
r.record_animal(dog)  # Recorded "Bark!"
r.record_animal(strange_animal)  # Recorded "Whooooo!!!"

    В этом примере мы создали родительский класс Mammal, содержащий voiceметод и два дочерних класса 
Dog: Cat. RecordКласс принимает animalобъект в качестве входных данных для record_animalметода и вызывает 
voice метод для вывода результата voiceвыполнения на консоль. В то же время существует Chupakabraкласс , 
который также имеет voiceметод , хотя он и не унаследован от Mammal. Однако объекты этого класса также 
могут быть переданы в record_animal. Главное, чтобы атрибут имел такое же имя и принимал те же аргументы 
(если это метод).

    Суть утиной типизации заключается не в том, чтобы заботиться о точном классе объекта, а в том, какие 
методы для него можно вызывать и какие операции можно над ним выполнять. Таким образом, вам просто нужно 
передать объект методу, зная, что при его неправильном использовании будет сгенерировано исключение. 

    Как мы уже упоминали, полиморфизм — это способность программы выбирать различные реализации при вызове 
операций с одним и тем же именем.

    Однако полиморфизм — это также способность объектов притворяться чем-то другим. В приведённом выше 
примере Chupakabra притворялись собакой и кошкой.

    Вам необходимо реализовать CatDogкласс без использования наследования от Animalкласса, но так, чтобы 
экземпляр класса CatDogвёл себя так же, как экземпляр класса Cat. Это означает, что он должен выдавать 
себя за Catкласс."""
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "Meow"

    def change_weight(self, weight):
        self.weight = weight
# Example usage
cat = Cat("Whiskers", 10)
cat_dog = CatDog("Fido", 15)
print(cat.say())  # Output: Meow
print(cat_dog.say())  # Output: Meow
print(cat.nickname)  # Output: Whiskers
print(cat_dog.nickname)  # Output: Fido
print(cat.weight)  # Output: 10
print(cat_dog.weight)  # Output: 15
cat_dog.change_weight(20)
print(cat_dog.weight)  # Output: 20

""" Реализуем Contactsкласс, работающий с контактами. На первом этапе добавим два метода.

A list_contacts возвращает список контактов — переменную contactsиз текущего экземпляра класса.
Добавляет add_contactsв список новый контакт, который является переменной объекта - contacts.
Класс Contacts содержит current_id переменную класса. Мы будем использовать её при добавлении нового 
контакта в качестве уникального идентификатора контакта. При добавлении нового контакта мы передаём 
методу следующие аргументы add_contacts: name, phone, email, и favorite. Метод должен создать словарь 
с указанными ключами и значениями параметров функции. Также необходимо добавить в словарь новый ключ 
идентификатора, значение которого будет значением current_id переменной класса.

Пример полученного словаря:

    {
    "id": 1,
    "name": "Wylie Pope",
    "phone": "(692) 802-2949",
    "email": "est@utquamvel.net",
    "favorite": True,
}
Добавляем указанный словарь в contacts список. Не забудьте увеличивать current_id переменную на единицу 
после каждого вызова метода add_contacts, чтобы ключ-идентификатор оставался уникальным для словаря.

ПРИМЕЧАНИЕ : Не создавайте экземпляр класса в коде, чтобы правильно пройти тест. """
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []
        

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(contact)
        Contacts.current_id += 1
# Example usage
contacts_manager = Contacts()
contacts_manager2 = Contacts()
contacts_manager3 = Contacts()

contacts_manager.add_contacts("Wylie Pope", "(692) 802-2949", "wpop@gmail.com", True)
contacts_manager2.add_contacts("John Doe", "(123) 456-7890", "John_Doe@gmail.com", False)
contacts_manager3.add_contacts("Serg Kalina", "(095) 456-7890", "Serg_Doe@Kalina.com", False)
print(contacts_manager.list_contacts())
print(contacts_manager2.list_contacts())
print(contacts_manager3.list_contacts())
  

"""                                     Розширене ООП в Python


                        Класи контейнери


    Часто для роботи потрібно створити об'єкти, які поводяться як стандартні контейнери Python, але з модифікованою
поведінкою. Ви, звичайно, можете спробувати наслідувати dict, str, list, але це може призвести до ряду непередбачених 
помилок. Правильний спосіб отримати модифікований контейнер — це використовувати пакет collections та класи UserList, 
UserDict, UserString, які в ньому є.
    Всі ці класи поводяться точно як вбудовані контейнери з тією лише відмінністю, що самі дані лежать у полі data у цих 
класів і ви можете використовувати це поле на свій розсуд.
    UserDict — це клас, що міститься в модулі collections і слугує обгорткою навколо словника. Він дозволяє легше 
створювати власні класи словників, модифікуючи або додаючи нову поведінку до стандартних методів словника."""

from collections import UserDict

class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value

# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict)

# Виведення:
# {'a': 1, 'b': 2, 'c': 3}
"""
    Ми створили клас MyDictionary, який наслідується від UserDict. Це надає всю стандартну функціональність словників, а також дозволяє легко модифікувати або розширювати її. Також ми додали метод add_key який демонструє, як можна додати нову поведінку для додавання елементів у словник.
Розглянемо більш корисний приклад. Ми маємо наступний список словників:

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]
    Ми хотіли б мати можливість, щоб у словника були методи які нам показували ім'я-телефон, та ім'я-email
контакту. Для цього створимо клас Customer, який наслідує від UserDict з модуля collections.

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"

    Він розширює можливості UserDict та має два методи: phone_info і email_info, кожен з яких повертає рядок 
з ім'ям та телефонним номером або електронною адресою відповідного контакту.
    Щоб скористатися можливостями створеного класу нам необхідно створити новий список customers, в якому кожен 
елемент списку contacts перетворюється на екземпляр класу Customer. Це дозволить нам використовувати визначені в 
класі методи для кожного контакту.

customers = [Customer(el) for el in contacts]

Повний код прикладу виглядатиме так:"""

from collections import UserDict

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"

if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())

# Виведення:
# ---------------------------
# Allen Raymond: (992) 914-3792
# Chaim Lewis: (294) 840-6685
# Kennedy Lane: (542) 451-7038
# ---------------------------
# Allen Raymond: nulla.ante@vestibul.co.uk
# Chaim Lewis: dui.in@egetlacus.ca
# Kennedy Lane: mattis.Cras@nonenimMauris.net

"""    У цьому прикладі ми двічі виконуємо ітерації по списку customers: перший раз для виведення інформації 
про телефони контактів через виклик методу phone_info, а другий раз - для виведення інформації про електронні 
адреси через виклик методу email_info.
    UserList - це клас, який дозволяє створювати власні версії списків з додатковими функціями. Ви можете додавати 
нові методи або змінювати ті, що вже існують, щоб вони працювали по-іншому. Це корисно, коли вам потрібен список, 
який робить щось спеціальне, чого не робить звичайний список Python.
    Простий приклад використання UserList:"""

from collections import UserList

class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)

# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)

# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)

# Виведення:
# Оригінальний список: [1, 2, 3]
# Оновлений список: [1, 2, 3, 4]
"""
    У цьому прикладі, клас MyList наслідує від UserList і додає метод add_if_not_exists, який дозволяє 
додати елемент до списку, лише якщо він ще не існує у списку. При цьому в іншому my_list веде себе як 
звичайний список.
    Наступний приклад:"""

from collections import UserList

class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))

countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())

# Виведення:15
"""
    У цьому прикладі ми створили клас, який поводиться як список, але в ньому є метод sum , який повертає суму 
всього вмісту цього класу, при цьому перетворюючи рядки на цілі числа.
    Останнім розглянемо UserString який є класом, аналогічним до UserList, але для рядків. Він дозволяє створювати 
класи, які наслідують поведінку звичайного рядка, з можливістю додавання нових методів або зміни стандартної 
поведінки рядків. Це корисно, коли вам потрібно працювати з рядками спеціалізованим чином, який не підтримується 
стандартними рядками Python.
    Розглянемо наступний приклад:"""
from collections import UserString

# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]

# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())

# Виведення:

# Рядок: radar
# Чи є паліндромом? True
# Рядок: hello
# Чи є паліндромом? False
"""
    У цьому прикладі, MyString наслідує від UserString і додає метод is_palindrome, який перевіряє, чи є 
рядок паліндромом (тобто читається однаково зліва направо та справа наліво).
    Останній приклад показує модифікований рядок з методом truncate, який обмежує розмір рядка до MAX_LEN символів."""

from collections import UserString

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('hello world!')
ts.truncate()
print(ts)

# Виведення:
# hello w """

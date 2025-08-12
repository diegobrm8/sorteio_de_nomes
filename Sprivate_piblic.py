class BankAccount:
    def __init__(self, account_number):
        self._account_number = account_number

    def _validate_account(self):
        print("Validating account...")


class SavingsAccount(BankAccount):
    def __init__(self, account_number):
        super().__init__(account_number)

    def calculate_interest(self):
        self._validate_account()
        print("Calculating interest...")


saving_account = SavingsAccount('123435')
print(saving_account._account_number)
saving_account._validate_account()
saving_account.calculate_interest()

print('-=' * 40)
print()


class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


person = Person("Alice")
# Atributos privados são prefixados com "__", o que indica que eles não devem ser acessados diretamente.
# No entanto, ainda é possível acessá-los usando _NomeDaClasse__nome_do_atributo.
print(person._Person__name)
print(person.get_name())
#print(person.__name)
print(person._Person__name)

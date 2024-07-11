import threading


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Внесена сумма в размере {amount} рублей. Баланс: {self.balance}')

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Снята сумма в размере {amount} рублей. Баланс: {self.balance}')
            else:
                print('Недостаточно средств')


ac_bank = BankAccount(1000)


def deposit_money():
    for _ in range(5):
        ac_bank.deposit(100)


def withdraw_money():
    for _ in range(3):
        ac_bank.withdraw(250)


thread1 = threading.Thread(target=deposit_money)
thread2 = threading.Thread(target=withdraw_money)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


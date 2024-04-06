from bank_accounts import *

Dave = BankAccount(1000,'Dave')
Sara = BankAccount(2000, 'Sara')

Dave.getBalance()
Sara.getBalance()

Dave.deposit(100)
Sara.deposit(500)

Dave.withdraw(10000)
Sara.withdraw(59000)
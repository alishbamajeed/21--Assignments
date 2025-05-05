class Bank:
  
    bank_name = "Standard Bank"

    @classmethod
    def change_bank_name(cls, name):
       
        cls.bank_name = name

bank1 = Bank()
bank2 = Bank()


print(f"Bank 1 Name: {bank1.bank_name}")  
print(f"Bank 2 Name: {bank2.bank_name}") 

Bank.change_bank_name("Global Bank")

print(f"Bank 1 Name after change: {bank1.bank_name}")  
print(f"Bank 2 Name after change: {bank2.bank_name}") 

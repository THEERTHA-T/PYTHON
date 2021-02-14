class bank:
    bal=0
    def __init__(self,nme,ac,typ,bal):
            self.name=nme
            self.acc_name=ac
            self.type=typ
            self.balance=bal
    def deposit(self):   
            amt=int(input("Enter the Amount to Deposit:"))
            self.balance+=amt
            print("\nNEW BALANCE = ",self.balance)
    def withdraw(self):
        if self.balance<500:
            print("\nInsufficient Balance..!!")
        else:
            amt=int(input("Enter the Amount to Withdraw:"))
            self.balance-=amt
            print("\nNEW BALANCE = ",self.balance)
    def disp(self):
            print("\nNAME = ",self.name)
            print("ACCOUNT NUMBER = ",self.acc_name)
            print("ACCOUNT TYPE = ",self.type)
            print("CURRENT BALANCE = ",self.balance)
    def bal(self):
            print("\nCURRENT BALANCE = ",self.balance)
            
n=input("Enter Name of the Account Holder :")
a=int(input("Enter Account Number :"))
t=input("Enter Account Type (CURRENT / SAVINGS) :")
bl=int(input("Enter Initial Amount:"))
b=bank(n,a,t,bl)

def choice():
    print("\nSELECT : \n1.DEPOSIT\n2.WITHDRAWAL\n3.BALANCE\n4.DISPLAY\n5.EXIT")
    ch=int(input("Enter your choice:"))
    
    if ch==1:
        b.deposit()
        choice()
    elif ch==2:
        b.bal()
        b.withdraw()
        choice()
    elif ch==3:
        b.bal()
        choice()
    elif ch==4:
        b.disp()
        choice()
    elif ch==5:
        print("EXITING..!")
        return 0
    else:
        print("Invalid Choice")
        return 0
choice()

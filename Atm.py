from copyreg import constructor
from urllib import response


class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balance(self):
        print("Your moneys is: 60000")    

    def withdrawl(self, cash):
        remainingMoney = 1000000000000 - cash
        print("You have withdrawn the amount: "+str(cash)+". Your Remaining Balance is: "+str(remainingMoney))


def main():
    numberOnCard = input("Insert your card no. ;) : ")
    pinNumber = input("What is your pin no. ;) : ")

    newUser = Atm(numberOnCard, pinNumber)
    print("Choose your activity")
    print("1: Balance Enquiry")
    print("2: Withdrawl")
    
    response = int(input("Enter the activity no.: "))
    if(response == 1):
        newUser.balance()
    elif(response ==2):
        amount = int(input("Enter the amount: "))
        newUser.withdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
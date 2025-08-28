class Atm:

    #function vs methods.
    #function is general or global and is used by any.
    #method is confined within a class and only used by that class objects.

    def __init__(self):#constructor--special method, tht is called as soon as u call the class using its obj created
        self.pin=""   #instance variables--executed or call as the class obj is called.
        self.balance=0

        self.menu()

        #print("hello friend!!")

    def menu(self):
        user_input=input("""How would you like to proceed:\n
                         1. Enter 1. to CREATE PIN \n
                         2. Enter 2. to DEPOSIT \n
                         3. Enter 3. to WITHDRAW \n
                         4. Enter 4. to CHECK BALANCE \n 
                         5. Enter 5. to EXIT \n""")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            print("WITHDRAW:")
        elif user_input=="4":
            print("CHECK BALANCE:")
        elif user_input=="5":
            print("EXIT:")
        else:
            print("THANKS FOR USING OUR SERVICE!!!!")
    
    def create_pin(self):
        self.pin=input("Enter the PIN: ")
        print("Pin set successfully!!")
    def deposit(self):
        temp=input("Enter your Pin:")
        if temp==self.pin:
            amt=int(input("Enter the amount: "))
            self.balance+=amt
            print("Deposit successfull!!")
        else:
            print("Incorrect Pin!!")
    def withdraw(self):

abc=Atm() #creating & calling obj for the given class.


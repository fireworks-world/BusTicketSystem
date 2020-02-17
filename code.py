print("-------------- Ticket management System -----------")
flag = True
while flag:
    print("====================")
    print("Enter your payment: ")
    print("Enter your seat no: ")
    print("Enter movie name: ")
    print("Enter 'Q' for quit: ")
    userChoice = input("Enter your choice: ")
    userPayment = input("Enter Payment: ")
    if 'Q' == userChoice or 'q' == userChoice:
        flag = False
        print("you can quit now...!!!")
    elif('A' == userChoice or 'a' == userChoice ):
        print("Your movie added")
    elif ('10.0' == userPayment or '10' == userPayment or '20.0' == userPayment or '20' == userPayment):
        print("Ticket price is " + userPayment)
    else:
        print("Invalid choice !!! Try Again")
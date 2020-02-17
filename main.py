#To make a console based Bus Ticket System where user can book a ticket and
#can check the status of the ticket. After booking a ticket the user will get
#a ticket in the console itself.
from logic import bookingData,busdisplay,ticketBook,displayticket,getDetails
print("-------Bus Ticket Booking------------");
flag=True
while flag:
    print("~~~~~~~~~~~~~~~~~~")
    print("--Press 'B' to Book Ticket--\n--Press 'S' to check Status--")
    option = input(">>>Enter your Choice:")
    if (option ==  'q' or option == 'Q'):
        print (">>>Thank You!!!")
        flag=False
    elif(option == 'b' or option == 'B'):
        busDetails=bookingData()
        filterData=busdisplay(busDetails)
        ticketbooking=ticketBook(filterData)
        displayticket(ticketbooking)

    elif(option == 's' or option == 'S'):
        getDetails()
    else:
        print(">>>Invalid Option!!! Please Try Again!!!")
from staticValue import busData
from random import randint as generator
def passengerData():
    name=input(">> Enter Your Name: ")
    phone=input(">> Enter Your Phone Number")
    return [name,phone]


def fromTo():
    location=input(">>>Enter From:")
    to=input(">>>Enter To:")
    date=input(">>>Enter Date:")
    return [location,to,date]


def bookingData():
    route=fromTo()
    buslist=[]
    for item in busData:
        if busData[item]['end']==route[1]:
            buslist.append(busData[item])
    data=passengerData()
    return data+buslist

def busdisplay(data):
    print("****Bus Details******\nName: {}\nPhone No. : {}\n-------------------".format(data[0],data[1]))
    slicedList=data[2:]
    i=1
    for item in slicedList:
        print(str(i)+"\nStart : {}\nEnd : {}\nFare : {}\nTime: {}".format(item['start'],item['end'],item['fare'],item['time']))
        i+=1
    userBus=int(input("Enter Bus Option: "))
    filterData=[data[0],data[1],slicedList[userBus-1]]
    return filterData

def ticketBook(filterData):
    noOftickets=int(input("Enter Total No. of Tickets:"))
    totalamount=noOftickets*filterData[2]['fare']
    print("Amount Payable: "+str(totalamount))
    userConfirmation=input("Do you Confirm the Booking(y/n): ")
    if userConfirmation=='y':
        return filterData+[totalamount,noOftickets]
    elif userConfirmation=='n':
        return False
def idmaker():
    id="CTS"+str(generator(100000,999999))
    return id


def datainsertion(bookingId, finalData):
    try:
        fopen=open("bookingData.txt",'a')
        string=[bookingId,finalData]
        fopen.write(str(string)+'\n')
    finally:
        fopen.close()
    return 1

def displayticket(finalData):
    bookingId=idmaker()
    savedata=datainsertion(bookingId,finalData)
    print("*********************************")
    print("Booking Id : {}\nName : {}\nBus No: {}".format(bookingId,finalData[0],finalData[2]['key']))


def datafromfile():
    try:
        fopen=open('bookingData.txt','r')
        data=fopen.read()
    finally:
        fopen.close()

    return data

def fetch(bookingId):
    data=datafromfile()
    return data

def getDetails():
    bookingId=input("Enter Booking Id: ")
    data=fetch(bookingId)
    print(type(data))


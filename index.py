from GymManager import GymManager
from Customer import Customer
from classes import Classes

gymManager = GymManager()



def menu():
    print ("\n")
    print ("##### Gym Management System #####")
    print ("\n")
    print ("1. Create Customer")
    print ("2. Create Classes")
    print ("3. Display all classes")
    print ("4. Display all customers")
    print ("5. Search customer by name")
    print ("6. Make Payment")
    print ("7. Process Payment")
    print ("8. Back to Menu")
    print ("\nEnter You Choice: ")

menu()

while(True):
    inp = int(input())
    if inp == 1:
        name = str(input("Enter customer's name - "))
        phoneNo = str(input("Enter customer's phone no. - "))
        joinDate = str(input("Enter joining date - "))
        customer = Customer(name, phoneNo, joinDate)
        gymManager.addCustomer(customer)

    elif inp == 2:
        type = str(input("Enter class - "))
        inhouseClass = str(input("Enter in-house class - "))
        room = str(input("Enter room number - "))
        instructor = str(input("Enter instructor name - "))
        cost = int(input("Enter class cost - "))
        classes = Classes(type, inhouseClass, cost)
        gymManager.addClasses(classes)

    elif inp == 3:
        print ("ClassesID\tType\tFacilities\tCost")
        for clsId in gymManager.classes.keys():
            classes = gymManager.classes[clsId]
            classesId = clsId
            type = classes.getType()
            facilities = classes.getFacilities()
            cost = classes.getCost()
            print (str(classesId) + "\t" + type + "\t" + facilities + "\t" + str(cost))

    elif inp == 4:
        print ("CustomerID\tName\tPhone\tJoining Date")
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            customerId = cusId
            name = customer.getName()
            phoneNo = customer.getPhoneNo()
            joinDate = customer.getJoiningDate()
            print (str(customerId) + "\t" + name + "\t" + phoneNo + "\t" + joinDate)

    elif inp == 5:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found".format(name))
        else:
            classesDict = gymManager.subscriptions.get(customerId)
            print ("Customer found", gymManager.customers[customerId])
            if classesDict != {}:
                print ("Subscribed to")
                for clsId in classesDict.keys():
                    print (gymManager.classes[clsId], "for {0} months".format(gymManager.subscriptions[customerId][classesId]))
            else:
                print ("No subscription found for this customer")

    elif inp == 6:
        name = str(input("Make payment via: - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found.".format(name))
            print ("Try adding a new customer.")
        else:
            print ("Customer found", gymManager.customers[customerId])
            if gymManager.classes.keys():
                for clsId in gymManager.classes.keys():
                    print (clsId, gymManager.classes[clsId])
                classesId = int(input("Select a class: "))
                if classesId > max(gymManager.classes.keys()):
                    print ("Please select a valid class.")
                else:
                    months = int(input("Enter no. of months"))
                    gymManager.addSubscription(gymManager.customers[customerId], gymManager.classes[classesId], months)
                    print ("Subscription added.")
            else:
                print ("No class exists. Try adding a class first.")

    elif inp == 7:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found.".format(name))
            print ("Try adding a new customer.")
        else:
            print ("Customer found", gymManager.customers[customerId])
            if gymManager.classes.keys():
                for clsId in gymManager.classes.keys():
                    print (clsId, gymManager.classes[clsId])
                classesId = int(input("Select a class"))
                if classesId > max(gymManager.classes.keys()):
                    print ("Please select a valid class.")
                else:
                    if gymManager.subscriptions[customerId][classesId] > 0:
                        customer = gymManager.customers[customerId]
                        classes = gymManager.classes[classesId]
                        gymManager.addPayment(customer, classes, classes.getCost())
                        print ("Payment added. Subscription expires in {0} months.".format(gymManager.subscriptions[customerId][classesId]))
    elif inp == 8:
        menu()
    elif inp == 9:
        gymManager.save()
        exit(0)
    else:
        print ("Please enter a valid number")
    menu()

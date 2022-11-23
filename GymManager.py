import pickle as cPickle
class GymManager:
    def __init__(self):
        self.customers = dict()
        self.classes = dict()
        self.subscriptions = dict()
        self.payments = dict()

    def addCustomer(self, customer):
        self.customers[customer.getCustomerId()] = customer
        self.subscriptions[customer.getCustomerId()] = dict()
        self.payments[customer.getCustomerId()] = dict()

    def addclasses(self, classes):
        self.classes[classes.getClassesId()] = classes

    def addSubscription(self, customer, classes, months):
        classesId = classes.getclassesId()
        customerId = customer.getCustomerId()
        self.subscriptions[customerId][classesId] = months

    def addPayment(self, customer, package, amount):
        classesId = classesId.getclassesId()
        customerId = customer.getCustomerId()
        self.payments[customerId][classesId] += amount
        self.subscriptions[customerId][classesId] -= 1

    def save(self):
        cPickle.dump(self, open("gym_manager.bin", "wb"))

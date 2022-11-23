from IDGenerator import IDGenerator


class Classes:
    def __init__(self, type, facilities, cost):
        self.__type = type
        self.__facilities = facilities
        self.__cost = cost
        self.__classesId = IDGenerator.generateCustomerID()

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setFacilities(self, facilities):
        self.__facilities = facilities

    def getFacilities(self):
        return self.__facilities

    def setCost(self, cost):
        self.__cost = cost

    def getCost(self):
        return self.__cost

    def getClassesId(self):
        return self.__classesId

    def __str__(self):
        return self.getType()+" "+str(self.getCost())+" "+self.getFacilities()+" "+str(self.getClassesId())
class computer:
    def __init__(self,getspecs,displayspecs):
        self.getspecs = getspecs
        self.displayspecs = displayspecs
    def getdata(self):
        self.getspecs = input("Enter the specs of RAM in GB: ")
        self.displayspecs = input("Enter display size in inch: ")
        print("The memory(RAM) in GB is: ",self.getspecs)
        print("The Display size in inch is: ", self.displayspecs)
obj = computer("","")
obj.getdata()

class desktop(computer):
    def __init__(self,spec1):
        self.spec1 = spec1
    def getdata(self):
        self.spec1 = input("Enter the weight of the desktop in Kg: ")
        print("The weight of desktop in Kg is: ", self.spec1)
obj1 = desktop("")
obj1.getdata()

class laptop(desktop):
    def __init__(self,spec2):
        self.spec2 = spec2
    def getdata(self):
        self.spec2 = input("Enter the weight of the laptop in Kg: ")
        print("The weight of desktop in Kg is: ", self.spec2)
obj2 = laptop("")
obj2.getdata()


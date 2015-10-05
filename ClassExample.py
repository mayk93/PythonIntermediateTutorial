from functools import reduce

class ExampleClass(object):
    def __init__(self,number):
        self.__number = number
        self.__string = "This class holds the number: "+str(self.number)
        self.__array = [reduce(lambda accumulatedValue,newValue: accumulatedValue+newValue , [x for x in range(self.number,end)],self.number) for end in range(self.number,self.number+10)]

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,value):
        self.__number = value if value >= 0 and value <= 1000 else 1
        self.__string = "This class holds the number: "+str(self.__number)
        self.__array = [reduce(lambda accumulatedValue,newValue: accumulatedValue+newValue , [x for x in range(self.number,end)],self.number) for end in range(self.number,self.number+10)]

    @property
    def string(self):
        return self.__string
    @string.setter
    def string(self,value):
        try:
            if type(int(value)) == type(0):
                self.number = int(value)
        except:
            pass

    @property
    def array(self):
        return self.__array
    @array.setter
    def array(self,value):
        try:
            if len(value) >= 1:
                self.number = value[0]
        except:
            pass

    def __str__(self):
        return "---\nObject:\nNumber: "+str(self.number)+"\nString: "+str(self.string)+"\nArray: "+str(self.array)+"\n---"

x = ExampleClass(5)
print(str(x))
x.number = 3
print(str(x))
x.string = "cdv"
print(str(x))
x.string = "5"
print(str(x))
x.array = [3,4,6,1]
print(str(x))

import math

def Clamp(value,start,end):
    if value < start:
        return start
    elif value > end:
        return end
    return value

class Vector3D(object):
    # Constructor
    def __init__(self,x=0.0,y=0.0,z=0.0,minX=-100,maxX=100,minY=-100,maxY=100,minZ=-100,maxZ=100):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ
        self.x = x
        self.y = y
        self.z = z
    # X Getter
    @property
    def x(self):
        return self.__x
    # X Setter
    @x.setter
    def x(self,value):
        self.__x = Clamp(value,self.minX,self.maxX)
    # Y Getter
    @property
    def y(self):
        return self.__y
    # Y Setter
    @y.setter
    def y(self,value):
        self.__y = Clamp(value,self.minY,self.maxY)
    # Z Getter
    @property
    def z(self):
        return self.__z
    # Z Setter
    @z.setter
    def z(self,value):
        self.__z = Clamp(value,self.minZ,self.maxZ)

    def __str__(self):
        return "< "+str(self.x)+","+str(self.y)+","+str(self.z)+" >"
    def __add__(self,other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z,minX,maxX,minY,maxY,minZ,maxZ)
    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def __sub__(self,other):
        return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z,minX,maxX,minY,maxY,minZ,maxZ)
    def __isub__(self,other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    def __mul__(self,other):
        if type(other) == type(0.0) or type(other) == type(0):
            return Vector3D(self.x*other,self.y*other,self.z*other,self.minX,self.maxX,self.minY,self.maxY,self.minZ,self.maxZ)
        else:
            newX = self.y*other.z - self.z*other.y
            newY = self.x*other.z - self.z*other.x
            newZ = self.x*other.y - self.y*other.x
            return Vector3D(newX,newY,newZ,self.minX,self.maxX,self.minY,self.maxY,self.minZ,self.maxZ)
    def __imul__(self,other):
        if type(other) == type(0.0) or type(other) == type(0):
            self.x *= other
            self.y *= other
            self.z *= other
            return self
        else:
            self.x = self.y*other.z - self.z*other.y
            self.y = self.x*other.z - self.z*other.x
            self.z = self.x*other.y - self.y*other.x
            return self

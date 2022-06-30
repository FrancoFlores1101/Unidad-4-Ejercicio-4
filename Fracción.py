class Fraccion:
    __numerador=0
    __denominador=0
    def __init__(self,n1,n2):
        self.__numerador=n1
        self.__denominador=n2
    def __mul__ (self,other):
        valor=str(int(self.__numerador)*int(other.__numerador))+"/"+str(int(self.__denominador)*int(other.__denominador))
        return valor
    def __add__(self,other):
        valor=str(int(self.__numerador)*int(other.__denominador)+int(self.__denominador)*int(other.__numerador))+"/"+str(int(self.__denominador)*int(other.__denominador))
        return valor
    def __floordiv__(self,other):
        valor=str(int(self.__numerador)*int(other.__denominador))+"/"+str(int(self.__denominador)*int(other.__numerador))
        return valor
    def __sub__(self,other):
        valor=str(int(self.__numerador)*int(other.__denominador)-int(self.__denominador)*int(other.__numerador))+"/"+str(int(self.__denominador)*int(other.__denominador))
        return valor


from functools import partial
from tkinter import ttk as tk
from tkinter import *
from Fracción import Fraccion
import re
class App:
    __num=0
    __ventana=None
    __entrada=None
    __index=0
    __operacion=0
    __segundonumero=0
    __operador=''
    __lista=[]
    __fraccion1=None
    __fraccion2=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry("316x260")
        self.__ventana.title("Calculadora")
        self.__ventana.resizable(0,0)
        self.__ventana.config(bg='light green')
        self.__entrada=Entry(self.__ventana,width=48,font=('Arial',8),bg='white',justify='right')
        self.__entrada.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        tk.Button(self.__ventana,text="C",command=partial(self.borrarTodo)).grid(row=2,column=0,pady=3,ipady=4)
        tk.Button(self.__ventana,text="<-",command=partial(self.borrarUno)).grid(row=2,column=1,pady=3,ipady=4)
        tk.Button(self.__ventana,text="%",command=partial(self.Dividir)).grid(row=2,column=3,pady=3,ipady=4)
        tk.Button(self.__ventana,text="-",command=partial(self.Restar)).grid(row=4,column=3,pady=3,ipady=4)
        tk.Button(self.__ventana,text="x",command=partial(self.Multiplicar)).grid(row=3,column=3,pady=3,ipady=4)
        tk.Button(self.__ventana,text="+",command=partial(self.Sumar)).grid(row=5,column=3,pady=3,ipady=4)

        tk.Button(self.__ventana,text="/",command=partial(self.ponernumeros,'/')).grid(row=2,column=2,pady=3,ipady=4)
        tk.Button(self.__ventana,text="1",command=partial(self.ponernumeros,'1')).grid(row=5,column=0,pady=3,ipady=4)
        tk.Button(self.__ventana,text="2",command=partial(self.ponernumeros,'2')).grid(row=5,column=1,pady=3,ipady=4)
        tk.Button(self.__ventana,text="3",command=partial(self.ponernumeros,'3')).grid(row=5,column=2,pady=3,ipady=4)
        tk.Button(self.__ventana,text="4",command=partial(self.ponernumeros,'4')).grid(row=4,column=0,pady=3,ipady=4)
        tk.Button(self.__ventana,text="5",command=partial(self.ponernumeros,'5')).grid(row=4,column=1,pady=3,ipady=4)
        tk.Button(self.__ventana,text="6",command=partial(self.ponernumeros,'6')).grid(row=4,column=2,pady=3,ipady=4)
        tk.Button(self.__ventana,text="7",command=partial(self.ponernumeros,'7')).grid(row=3,column=0,pady=3,ipady=4)
        tk.Button(self.__ventana,text="8",command=partial(self.ponernumeros,'8')).grid(row=3,column=1,pady=3,ipady=4)
        tk.Button(self.__ventana,text="9",command=partial(self.ponernumeros,'9')).grid(row=3,column=2,pady=3,ipady=4)
        tk.Button(self.__ventana,text="0",command=partial(self.ponernumeros,'0')).grid(row=6,column=0,pady=3,ipady=4,ipadx=40,columnspan=3)

        tk.Button(self.__ventana,text="=",command=partial(self.Igual)).grid(row=6,column=3,pady=3,ipady=4)

        self.__ventana.mainloop()
    def ponernumeros(self,num):
        self.__entrada.insert(self.__index,num)
        self.__index+=1
    def borrarTodo(self):
        self.__index=0
        self.__entrada.delete(0,END)
    def borrarUno(self):
        num=int(self.__index)-1
        self.__entrada.delete(num)
        self.__index-=1
    def getprimer(self):
        self.__primernumero=int(self.__entrada.get())
        self.__entrada.delete(0,END)
        self.__index=0
    def conviertefraccion(self):
        listanumeros=str(self.__entrada.get())
        match=re.findall('[-0-9]+',listanumeros)
        self.__lista.append(match)
        self.__entrada.delete(0,END)
        self.__index=0
    def Dividir(self):
        try:
            self.__operador='division'
            self.getprimer()
        except:
            self.__operador='division'
            self.conviertefraccion()
            pass
    def Sumar(self):
        try:
            self.__operador='suma'
            self.getprimer()
        except:
            self.__operador='suma'
            self.conviertefraccion()
            pass
    def Multiplicar(self):
        try:
            self.__operador='multiplicacion'
            self.getprimer()
        except:
            self.__operador='multiplicacion'
            self.conviertefraccion()
            pass
    def Restar(self):
        try:
            self.__operador='resta'
            self.getprimer()
        except:
            self.__operador='resta'
            self.conviertefraccion()
            pass
    def CrearFracciones(self):
        listanumeros=str(self.__entrada.get())
        match=re.findall('[-0-9]+',listanumeros)
        self.__lista.append(match)
        Numerador1=self.__lista[0][0]
        Denominador1=self.__lista[0][1]
        Numerador2=self.__lista[1][0]
        Denominador2=self.__lista[1][1]
        self.__fraccion1=Fraccion(Numerador1,Denominador1)
        self.__fraccion2=Fraccion(Numerador2,Denominador2)
        self.__lista.clear()
    def Igual(self):
        try:
            if self.__operador=='dividision':
                try:
                    self.__segundonumero=int(self.__entrada.get())
                    if self.__segundonumero!=0:
                            resultado=self.__primernumero/self.__segundonumero
                            self.__entrada.delete(0,END)
                            self.__entrada.insert(0,resultado)
                    else:
                        resultado="ERROR division por 0"
                        self.__entrada.delete(0,END)
                        self.__entrada.insert(0,resultado)
                except:
                    self.CrearFracciones()
                    r=self.__fraccion1//self.__fraccion2
                    self.__entrada.delete(0,END)
                    resultado=self.simplificar(r)
                    self.__entrada.insert(0,resultado)
            elif self.__operador=='suma':
                try:
                    self.__segundonumero=int(self.__entrada.get())
                    result=self.__primernumero+self.__segundonumero
                    self.__entrada.delete(0,END)
                    self.__entrada.insert(0,result)
                except:
                    self.operacion()
                    r=self.__fraccion1+self.__fraccion2
                    self.__entrada.delete(0,END)
                    result=self.simplificar(r)
                    self.__entrada.insert(0,result)
            elif self.__operador=='multiplicacion':
                try:
                    self.__segundonumero=int(self.__entrada.get())
                    result=self.__primernumero*self.__segundonumero
                    self.__entrada.delete(0,END)
                    self.__entrada.insert(0,result)
                except:
                    self.operacion()
                    r=self.__fraccion1*self.__fraccion2
                    self.__entrada.delete(0,END)
                    result=self.simplificar(r)
                    self.__entrada.insert(0,result)
            elif self.__operador=="resta":
                try:
                    self.__segundonumero=int(self.__entrada.get())
                    result=self.__primernumero-self.__segundonumero
                    self.__entrada.delete(0,END)
                    self.__entrada.insert(0,result)
                except:
                    self.operacion()
                    r=self.__fraccion1-self.__fraccion2
                    self.__entrada.delete(0,END)
                    result=self.simplificar(r)
                    self.__entrada.insert(0,result)
            r=str(resultado)
            self.__index=len(r)
            self.__primernumero=0
            self.__segundonumero=0
        except:
            pass

    def simplificar(self,fraccion):
        numeros=re.findall('[-0-9]+',fraccion)
        numerador=int(numeros[0])
        denominador=int(numeros[1])
        i=2
        while i<9:
            if numerador%i==0 and denominador%i==0:
                numerador//=i
                denominador//=i
            else:
                i+=1
        if denominador ==1:
            retorno=str(numerador)
        else:
            retorno=str(numerador)+'/'+str(denominador)
        return retorno
if __name__=='__main__':
    app=App()

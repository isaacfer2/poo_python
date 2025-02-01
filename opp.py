#!/usr/bin/python3

class Calculadora:
    def __init__(self, num1):
        self.num1 = num1

    def suma(self, num2):
        return self.num1 + num2 #8 + 4 = 12

    def suma_doble(self,num1, num2): #Calculadora.suma_doble(calc, 3, 5)
        print(self.suma(num1) + self.suma(num2)) # 5 + 2 = 7 | 5 + 9 = 14  

calc = Calculadora(5)

calc.suma(4)

calc.suma_doble(2,9)

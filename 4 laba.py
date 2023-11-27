class Lighter:
    def __init__(self,type,power,amount,name_productoin,number,line):
        self.__type = type
        self.__power = power
        self.__amount = amount
        self.__name_production = name_productoin
        self._number = number
        self._line = line
    def get_type(self):
        return self.__type
    def get_power(self):
        return self.__power
    def get_amount(self):
        return self.__amount
    def get_name_production(self):
        return self.__name_production
    def __str__(self):
        return f"Світильник: {self.__name_production}, {self.__type}"
    def __repr__(self):
        return f"світильник('{self.__type}' , {self.__power}, {self.__amount}, '{self.__name_production}')"
    def __del__(self): 
        print(f"Об'єкт {self} був видалений") 
 
    def get_number(self): 
        return self._number 
 
    def get_line(self): 
        return self._line 
 
if __name__ == "__main__": 
    lighter_1 = Lighter("настінний", 60, 4, "Philips", 5, "Hello") 
    lighter_2 = Lighter("підвісний", 40, 3, "Osram", 10, "World") 
    lighter_3 = Lighter("настільний", 30, 2, "General Electric", 15, "Python") 
 
    print(lighter_1.get_type())   
    print(lighter_1.get_power())   
    print(lighter_1.get_amount())   
    print(lighter_1.get_name_production())    
    print(lighter_1.get_number()) 
    print(lighter_1.get_line()) 
 
    print(lighter_2.get_type())   
    print(lighter_2.get_power())   
    print(lighter_2.get_amount())   
    print(lighter_2.get_name_production()) 
    print(lighter_2.get_number())   
    print(lighter_2.get_line()) 
 
    print(lighter_3.get_type())   
    print(lighter_3.get_power())   
    print(lighter_3.get_amount())   
    print(lighter_3.get_name_production()) 
    print(lighter_3.get_number())   
    print(lighter_3.get_line())

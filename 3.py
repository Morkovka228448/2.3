class Calculation:


    def __init__(self,calculation_line=""):
        self.__calculationLine = calculation_line

    def set_calculation_line(self, new_calculation_line):
        self.__calculationLine = new_calculation_line

    def set_last_symbol_calculation_line(self, symbol):
        self.__calculationLine += symbol

    def get_calculation_line(self):
        return self.__calculationLine

    def get_last_symbol(self):

        if self.__calculationLine:
            return self.__calculationLine[-1]
        else:
            return None

    def delete(self):

        if self.__calculationLine:
            self.__calculationLine = self.__calculationLine[:-1]

    def __str__(self):
        return f"Calculation Line: {self.__calculationLine}"


calc = Calculation("2 + 2")

print(f"Текущая строка: {calc.get_calculation_line()}")

calc.set_last_symbol_calculation_line(" * 3")
print(f"Строка после добавления символа: {calc.get_calculation_line()}")

last_symbol = calc.get_last_symbol()
print(f"Последний символ: {last_symbol}")

calc.delete()
print(f"Строка после удаления последнего символа: {calc.get_calculation_line()}")

calc.set_calculation_line("10 / 5")
print(f"Новая строка: {calc.get_calculation_line()}")

print(calc)

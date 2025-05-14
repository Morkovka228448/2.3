class Worker:
    def __init__(self, name, surname, rate, days):

        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):

        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days

    def get_salary(self):
        return self.__rate * self.__days

    def __str__(self):
        return f"Worker: {self.__name} {self.__surname}, Rate: {self.__rate}, Days: {self.__days}, Salary: {self.get_salary()}"

worker = Worker("Cергей", "Иванов", 3200, 20)


print(f"Имя: {worker.get_name()}")
print(f"Фамилия: {worker.get_surname()}")
print(f"Ставка: {worker.get_rate()}")
print(f"Отработанные дни: {worker.get_days()}")

salary = worker.get_salary()
print(f"Зарплата работника: {salary}")
print(worker)

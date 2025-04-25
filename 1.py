class Worker:

    def __init__(self, name, surname, rate, days):

        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):

        return self.rate * self.days
    def __str__(self):
      return f"Worker: {self.name} {self.surname}, Rate: {self.rate}, Days: {self.days}, Salary: {self.get_salary()}"

worker = Worker("Влад", "Курденевич", 3200, 20)
salary = worker.get_salary()
print(f"Зарплата работника: {salary}")
print(worker)
class Employee:
    def calculate_salary(self):
        print("Calculating salary for general employee")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for manager with bonus")

emp = Employee()
mgr = Manager()
emp.calculate_salary()
mgr.calculate_salary()
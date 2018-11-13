class Employee:
    """
    the base class
    """
    nextId = 0

    def __init__(self, name):
        self.name = name
        self.id = Employee.nextId
        Employee.nextId += 1

        # Created to use the overload function
        self.weekly_wage = 0

    def get_name(self):
        return self.name

    def weekly_pay(self, hours_worked):
        return 0
    
    # Overload
    def __lt__(self, another_employee):
        """
        Returns true if an employee's weekly wage is lower than another employee's weekly pay, assuming only 40 hours worked.
        """
        return self.weekly_wage < another_employee.weekly_wage


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        self.weekly_wage = hours_worked * self.hourly_rate + (hours_worked - 40) * .5*(self.hourly_rate) if hours_worked > 40 else hours_worked * self.hourly_rate
        return self.weekly_wage


class Exempt_Employee(Employee):
    
    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary
    
    def weekly_pay(self, hours_worked):
        self.weekly_wage = (self.annual_salary)/(52.0)
        return self.weekly_wage



class Manager(Exempt_Employee):
    
    def __init__(self, name, annual_salary, bonus):
        Exempt_Employee.__init__(self, name, annual_salary)
        self.bonus = bonus
    
    def weekly_pay(self, hours_worked):
        self.weekly_wage = (self.annual_salary + self.bonus)/(52.0)
        return self.weekly_wage


def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)
    
    print(all_employees[0] < all_employees[1])


if __name__ == '__main__':
    main()

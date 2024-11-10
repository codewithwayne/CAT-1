class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to {self.salary}.")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to the {self.department_name} department.")

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total_salary}")

    def display_all_employees(self):
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_details()


dept = Department("Tech")

while True:
    action = input("\nEnter 'add' to add an employee, 'update' to update salary, 'total' to see total salary, 'list' to display all employees, or 'quit' to exit: ").strip().lower()

    if action == 'add':
        name = input("Enter employee's name: ")
        employee_id = input("Enter employee's ID: ")
        salary = float(input("Enter employee's salary: "))
        employee = Employee(name, employee_id, salary)
        dept.add_employee(employee)

    elif action == 'update':
        employee_id = input("Enter the employee ID for salary update: ")
        new_salary = float(input("Enter the new salary: "))
        for employee in dept.employees:
            if employee.employee_id == employee_id:
                employee.update_salary(new_salary)
                break
        else:
            print("Employee not found.")

    elif action == 'total':
        dept.calculate_total_salary()

    elif action == 'list':
        dept.display_all_employees()

    elif action == 'quit':
        print("Exiting program.")
        break

    else:
        print("Invalid action. Please try again.")

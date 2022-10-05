class employee:
    def __init__(self,employee_name,employee_num):
        self.employee_name = employee_name
        self.employee_num = employee_num

class productionWorker(employee):
    def __init__(self,employee_name,employee_num,shiftNum,hourPay):
        self.shiftNum = shiftNum
        self.hourPay = hourPay
        employee.__init__(self,employee_name,employee_num)

    @classmethod 
    def from_input(cls):
        return cls(
            input("Enter employee name: "),
            input("Enter employee number: "),
            int(input("Enter shift number: ")),
            float(input("Enter hourly wage: "))
        )

    def __str__(self):
        return f"{self.employee_name}, {self.employee_num}, {self.shiftNum}, {self.hourPay}"
 
my_productionWorker = productionWorker(1,2,3,4)

print(my_productionWorker)

proWorker = productionWorker.from_input()

print(proWorker)


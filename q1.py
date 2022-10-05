class person():
    def __init__(self,name,address,phone_num):
        self.name = name
        self.address = address 
        self.phone_num = phone_num
my_person = person(name='David',address='7552 Rushing River dr.',phone_num='876-567-8893')
type(my_person)

class customer(person):
    def __init__(self,customer_num,mail_list):
        self.customer_num = customer_num
        self.mail_list = mail_list
my_customer = customer(customer_num='65475',mail_list=True)

print(my_customer.customer_num,my_customer.mail_list)

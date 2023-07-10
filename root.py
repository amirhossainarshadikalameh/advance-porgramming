class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name=name
        self.amount=amount
        self.price=price
        pass


class Pharmacy:
    def __init__(self, name: str):
        self.name=name
        self.drugs=[]
        self.employees=[]

        pass

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)
        pass

    def add_employee(self, first_name: str, last_name: str, age: int):
        self.employees.append({"first_name":first_name,"last_name":last_name, "age":age})

        pass

    def total_value(self) -> int:
        sum_amount=0
        for drug in self.drugs:
            sum_amount+=(drug.amount)*(drug.price)
        return sum_amount


        pass

    def employees_summary(self) -> str:
        line ='Employees:'+'\n'
        number=0
        for employ in self.employees:
            number+=1
            line+=f"The employee number {number} is {employ['first_name']} {employ['last_name']} who is {employ['age']} years old."+'\n'
        return line
        pass

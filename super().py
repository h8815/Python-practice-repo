class Laptop:
    def __init__(self,company,spec,processor):
        self.company = company
        self.spec = spec
        self.processor = processor 
        print("Laptop is an electronic device")
    @staticmethod
    def start():
        print("Laptop start")

class Company(Laptop):
    def __init__(self, company, spec, processor):
        super().__init__(company, spec, processor)
        print(f"Company {company}\nSpecification {spec}\nProcessor {processor}")
        super().start()

c1 = Company("Lenovo","15 inch","Ryzen 7")

